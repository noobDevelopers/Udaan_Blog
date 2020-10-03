from django.shortcuts import render,HttpResponseRedirect
from .models import Blogs,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.urls import reverse
from taggit.models import Tag
from django.db.models import Count

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


def home(request,tag_slug = None):
    #list of all published posts in order of publish date
    object_list = Blogs.published.all().order_by('-publish')
    tag = None
    #if search by tag is clicked
    if tag_slug:
        tag = get_object_or_404(Tag,slug = tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list,3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    
    #for searching
    query = None
    #search results
    results = []
    #if search button is pressed
    if 'search' in request.GET:
        query = request.GET['search']
        
           
        search_vector = SearchVector('title', weight='A') + SearchVector('body', weight='B') 
        search_query = SearchQuery(query)
        #return search results
        results = Blogs.objects.annotate( rank=SearchRank(search_vector, search_query) ).filter(rank__gte=0.3).order_by('-rank')
        return render(request,'blogs/search.html',{'results':results,'query':query,})
    return render(request,'blogs/home.html',{'posts':posts,'tag':tag,})

def detail(request,year,month,day,post):
    # get the current post
    post = get_object_or_404(Blogs,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    # get first three latest posts
    latest_posts = Blogs.published.all().order_by('-publish')[:3]
    all_tag = Tag.objects.all()
    # get all comments related to current post
    comments = post.comments.filter(active = True)
    new_comment = None
    # add new comment
    if request.method == 'POST':
       new_comment = Comment()
       new_comment.name = request.POST['name']
       new_comment.email = request.POST['email']
       new_comment.body = request.POST['body'] 
       new_comment.post = post
       new_comment.save()
      
       return HttpResponseRedirect(post.get_absolute_url())
    post_tags_ids = post.tags.values_list('id',flat = True)
    # similar posts is decide by the tags, top 4 posts with matching tags and publish
    # date are stored in similar_posts 
    similar_posts = Blogs.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]
    
    query = None
    results = []
    #seach
    if 'search' in request.GET:
        query = request.GET['search']
        
            
        search_vector = SearchVector('title', weight='A') + SearchVector('body', weight='B') 
        search_query = SearchQuery(query)

        results = Blogs.objects.annotate( rank=SearchRank(search_vector, search_query) ).filter(rank__gte=0.3).order_by('-rank')
        return render(request,'blogs/search.html',{'results':results,'query':query,})
    return render(request,'blogs/detail.html',{'post':post,'latest_posts':latest_posts,'comments':comments,'new_comment':new_comment,'tags':all_tag,'similar_posts':similar_posts,})




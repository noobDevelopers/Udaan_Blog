from django import template
register = template.Library()
from ..models import Blogs
from django.db.models import Count
@register.filter
def getavat(image,counter):
    
    counter_edit = counter%5
    if counter_edit == 0:
        counter_edit=5
    counter_edit = str(counter_edit)
    result = image[0:image.find('_')+1]+counter_edit+image[image.find('_')+1:]
    return result

@register.simple_tag
def get_most_commented_posts(count=5):
    return Blogs.published.annotate(
        total_comments = Count('comments')
    ).order_by('-total_comments')[:count]
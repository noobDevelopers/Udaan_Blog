from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Blogs

class LatestPostsFeed(Feed):
    title = 'Blog'
    link = ''
    description = 'New posts of my Blog'

    def items(self):
        return Blogs.published.all()[:5]
    def item_title(self , item):
        return item.title
    def item_description(self , item):
        return truncatewords(item.body , 30)
    



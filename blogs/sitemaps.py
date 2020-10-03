from django.contrib.sitemaps import Sitemap
from .models import Blogs

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Blogs.published.all()
    
    def lastmod(self , obj):
        return obj.updated
        
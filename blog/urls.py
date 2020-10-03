"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
import ckeditor_uploader
from django.contrib.sitemaps.views import sitemap 
from blogs.sitemaps import PostSitemap
from django.views.decorators.cache import never_cache

from ckeditor_uploader import views

sitemaps = {
    'post':PostSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blogs.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns_ck = [
    re_path(r'^upload/', views.upload, name='ckeditor_upload'),
    re_path(r'^browse/', never_cache(views.browse), name='ckeditor_browse'),
]

urlpatterns = urlpatterns+urlpatterns_ck


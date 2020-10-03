from django.urls import path
from blogs import views
from .feeds import LatestPostsFeed
urlpatterns = [
    path('',views.home,name='home'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.detail, name='detail'),
    path('tag/<slug:tag_slug>/', views.home, name='post_list_by_tag'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
   
]
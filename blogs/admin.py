from django.contrib import admin
from .models import Blogs,Comment
@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title','author','slug','publish','status')
    list_filter = ('status','author','publish')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status','publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','post','created','active')
    list_filter = ('active','created','updated')
    search_fields = ('name','email','body')
# Register your models here.

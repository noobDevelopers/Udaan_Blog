from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')
class Blogs(models.Model):
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique_for_date='publish')
    image = models.ImageField(upload_to='posts/')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body = RichTextUploadingField()
    publish = models.DateTimeField(default= timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    read_time = models.IntegerField(default=0)
    small_title = models.CharField(max_length=15)
    def get_absolute_url(self):
        return reverse('detail',
                    args = [self.publish.year,
                            self.publish.month,
                            self.publish.day,
                            self.slug])
    def date(self):
        return self.publish.strftime("%d/%m/%Y")
    
    #November 13, 2019 at 2:21pm
    def day(self):
        return self.publish.strftime("%d")
    
    def year(self):
        return self.publish.strftime("%Y")

    def month(self):
        return self.publish.strftime("%B")
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(Blogs,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def date(self):
        hour = int(self.created.strftime("%I"))+5
        minute = int(self.created.strftime("%M"))+30
        return self.created.strftime(f"%B %d, %Y at {hour}:{minute}%p")#%B %d, %Y at %I:%M%p"
    class Meta:
        ordering = ('created',)
    def __str__(self):
        return f"Comment by {self.name} on {self.post}"
# Create your models here.

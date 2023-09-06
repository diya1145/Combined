from django.conf import settings
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
import csv


class Category(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True, null=True, blank=True) 
    text = models.TextField()   
    image = models.ImageField(upload_to='media/thumbnail',blank=True, null=True)
    future_image = models.ImageField(upload_to='media/future_image',blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)

    @property
    def number_of_comments(self):
        return post_detail.objects.filter(post_comment=self).count()
     
class RegistrationForm(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
 
class login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class update(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
   

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    reply  = models.ForeignKey('self', related_name='replies', on_delete=models.PROTECT ,null=True , blank=True)

    def __str__(self):
        return 'Comment by {}'.format(self.author)

    
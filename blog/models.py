from django.conf import settings
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
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

class User(AbstractUser):
        GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
        )
        STATE_CHOICES = (
            ("rajasthan", "rajasthan"),
            ("punjab", "punjab"),
            ("uttarpradesh", "uttarpradesh"),
        )
        username = models.CharField(max_length=50, blank=True, null=True, unique=True)
        email = models.EmailField(unique=True)
        user_profile = models.ImageField(upload_to='avatar', blank=True, null=True)
        city = models.CharField(max_length=200)
        gender = models.CharField(max_length=200, choices=GENDER_CHOICES, default='')
        state = models.CharField(max_length=200, choices=STATE_CHOICES, default='')
        dob = models.DateField(null=True, blank=True)
        country = models.CharField(max_length=200)
        zip_code = models.IntegerField(null=True)
        phone_no = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(9999999999)])

    
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    reply  = models.ForeignKey('self', related_name='replies', on_delete=models.PROTECT ,null=True , blank=True)

    def __str__(self):
        return 'Comment by {}'.format(self.author)



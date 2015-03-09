from django.db import models
from django.utils import timezone


class Post(models.Model):
  author = models.CharField(max_length=200)
  title = models.CharField(max_length=200)
  text = models.CharField(max_length=2000)
  pub_date = models.DateTimeField(default=timezone.now)
  upd_date = models.DateTimeField(default=timezone.now)
  is_public = models.BooleanField(default=True)


class Comment(models.Model):
  author = models.CharField(max_length=200)
  text = models.CharField(max_length=2000)
  pub_date = models.DateTimeField(default=timezone.now)
  post = models.ForeignKey(Post)


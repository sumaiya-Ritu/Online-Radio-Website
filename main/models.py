from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
  content = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  like = models.ManyToManyField(User, related_name='comment_like', blank=True)

  def total_likes(self):
      return self.like.count()

class Reply(models.Model):
  content = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  like = models.ManyToManyField(User, related_name='reply_like', blank=True)

  def total_likes(self):
      return self.like.count()
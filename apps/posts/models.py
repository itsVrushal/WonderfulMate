from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    visibility = models.CharField(max_length=20, choices=(('public','Public'), ('friends','Friends')) , default='public')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    # Note: Comments are only visible to post owner per your spec. Enforce in serializers/views.
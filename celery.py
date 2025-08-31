import os
from celery import Celery  # <-- make sure it's capital C

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wonderfulmate.settings')

app = Celery('wonderfulmate')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()





### FILE: apps/users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
# Extend as necessary. Username/email already available.
    pass


class UserProfile(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='profile')
    about = models.TextField(blank=True)
    interests = models.JSONField(default=list) # list of strings
    hobbies = models.TextField(blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    xp = models.FloatField(default=0.0)
    reveal_level = models.IntegerField(default=0)
    # store embedding vectors or pointers to external store
    about_embedding = models.BinaryField(null=True, blank=True)


    def location_tuple(self):
        return (self.lat, self.lon) if self.lat and self.lon else None


class Telemetry(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='telemetry')
    avg_response_time = models.FloatField(default=10.0)
    avg_msg_length = models.FloatField(default=20.0)
    pause_pattern = models.JSONField(default=dict) # arbitrary telemetry summaries


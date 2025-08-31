from django.db import models


class Message(models.Model):
    sender = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, related_name='received_messages')
    text = models.TextField(blank=True)
    emoji = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
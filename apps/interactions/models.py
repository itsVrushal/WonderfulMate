from django.db import models


class Friendship(models.Model):
    from_user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, related_name='outgoing_requests')
    to_user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, related_name='incoming_requests')
    status = models.CharField(max_length=20, choices=(('pending','pending'),('accepted','accepted'),('rejected','rejected')) , default='pending')
    created_at = models.DateTimeField(auto_now_add=True)


class Interaction(models.Model):
    # Generic interaction record for XP computation
    actor = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, related_name='interactions')
    target = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, related_name='interacted_with')
    type = models.CharField(max_length=20, choices=(('like','like'),('comment','comment'),('chat','chat'),('game','game')))
    value = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
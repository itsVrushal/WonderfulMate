from django.db import models


class GameSession(models.Model):
    players = models.ManyToManyField('users.UserProfile')
    state = models.JSONField(default=dict)
    winner = models.ForeignKey('users.UserProfile', on_delete=models.SET_NULL, null=True, blank=True, related_name='won_games')
    xp_reward = models.FloatField(default=5.0)
    created_at = models.DateTimeField(auto_now_add=True)
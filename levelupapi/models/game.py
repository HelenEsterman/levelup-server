from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games")
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name="games")
    rules = models.CharField(max_length=600)
    number_of_players = models.IntegerField(blank=False)
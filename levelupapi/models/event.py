from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=200)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    gamers_attending = models.ManyToManyField(User, through= "EventGamer", related_name="events_gamer_is_attending")
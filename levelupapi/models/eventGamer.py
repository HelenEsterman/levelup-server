from django.db import models
from django.contrib.auth.models import User

class EventGamer(models.Model):
    gamer = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    participants = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class Message(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.content

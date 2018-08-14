import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from background_task import background

from api.chat.models import Message


@receiver(post_save, sender=Message)
def push_notification(sender, instance, **kwargs):
    msg = instance
    rest = msg.room.participants.exclude(id=msg.sender.id).all()
    for person in rest:
        push(to=person.id, content=msg.content)


@background
def push(to, content):
    data = {
        'device_id': to,
        'content': content,
    }
    try:
        requests.post('localhost:7000', json=data)
    except requests.exceptions.InvalidSchema:
        pass

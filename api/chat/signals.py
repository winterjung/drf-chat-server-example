from django.db.models.signals import post_save
from django.dispatch import receiver

from api.chat.models import Message
from api.chat.tasks import push


@receiver(post_save, sender=Message)
def push_notification(sender, instance, **kwargs):
    msg = instance
    rest = msg.room.participants.exclude(id=msg.sender.id).all()
    for person in rest:
        push(to=person.id, content=msg.content)

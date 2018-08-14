from django.conf import settings
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from django.utils import timezone

from api.chat.models import Message
from api.chat.tasks import push, msg_remover


@receiver(post_save, sender=Message)
def push_notification(sender, instance, **kwargs):
    msg = instance
    rest = msg.room.participants.exclude(id=msg.sender.id).all()
    for person in rest:
        push(to=person.id, content=msg.content)


@receiver(post_migrate)
def start_tasks(sender, **kwargs):
    lifetime = settings.MSG_LIFETIME
    msg_remover(
        lifetime,
        repeat=lifetime / 10,
        schedule=dict(
            run_at=timezone.now(),
            action=1,
        ),
    )

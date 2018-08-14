from datetime import timedelta

import requests
from background_task import background
from django.utils import timezone

from api.chat.models import Message


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


@background
def msg_remover(lifetime):
    deadline = timezone.now() - timedelta(seconds=lifetime)
    Message.objects.filter(created_at__lt=deadline).delete()

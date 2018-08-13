import pytest
from rest_framework.test import APIClient

from api.chat.models import Message, Room, User


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def users():
    u1 = User.objects.create(username='001')
    u1.set_password('001')
    u1.save()
    u2 = User.objects.create(username='002')
    u2.set_password('002')
    u2.save()
    return (u1, u2)


@pytest.fixture
def another_user():
    u = User.objects.create(username='003')
    u.set_password('003')
    u.save()
    return u


@pytest.fixture
def room(users):
    r = Room.objects.create(title='test001')
    r.participants.set(users)
    return r


@pytest.fixture
def msg(users, room):
    m = Message(content='hello', room=room, sender=users[0])
    m.save()
    return m


@pytest.fixture
def conversation(users, room):
    Message.objects.create(content='hello', room=room, sender=users[0])
    Message.objects.create(content='world', room=room, sender=users[1])
    Message.objects.create(content='how are you?', room=room, sender=users[0])
    Message.objects.create(content='im good', room=room, sender=users[1])
    Message.objects.create(content='see you later', room=room, sender=users[0])
    Message.objects.create(content='bye', room=room, sender=users[1])

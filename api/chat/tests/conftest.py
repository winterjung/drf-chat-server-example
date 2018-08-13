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
def room(users):
    r = Room.objects.create(title='test001')
    r.participants.set(users)
    return r


@pytest.fixture
def msg(users, room):
    m = Message(content='hello', room=room, sender=users[0])
    m.save()
    return m

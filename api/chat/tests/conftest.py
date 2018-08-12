import pytest

from api.chat.models import Message, Room, User


@pytest.fixture
def users(django_db_setup):
    u1 = User.objects.create(username='001')
    u2 = User.objects.create(username='002')
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

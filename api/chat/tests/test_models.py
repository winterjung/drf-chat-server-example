import pytest

from api.chat.models import Message, Room, User


@pytest.mark.django_db
class TestBasicModels:
    def test_new_user(self, users):
        assert users[0].username == '001'
        assert users[1].username == '002'
        assert User.objects.count() == 2

    def test_new_room(self, users, room):
        assert room.id == 1
        assert room.title == 'test001'
        assert room.participants.count() == 2
        assert users[0].room_set.count() == 1
        assert users[1].room_set.count() == 1

    def test_new_msg(self, msg):
        assert msg.id == 1
        assert msg.content == 'hello'
        assert msg.room.id == 1
        assert msg.sender.id == 1

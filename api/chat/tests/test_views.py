import pytest

from api.chat.models import Room
from api.chat.tests.utils import LoginableTestCase


@pytest.mark.django_db
class TestRoomView(LoginableTestCase):
    def test_room_list_without_data(self, users):
        self.login('001', '001')
        res = self.client.get('/v1/rooms/')
        assert res.status_code == 200
        assert res.data == []

    def test_room_list_with_data(self, room):
        self.login('001', '001')
        res = self.client.get('/v1/rooms/')
        assert res.status_code == 200
        data = res.json()
        assert len(data) == 1

        room = data[0]
        assert room['id'] == 1
        assert room['title'] == 'test001'
        assert len(room['participants']) == 2
        assert room['participants'][0] == 1
        assert room['participants'][1] == 2

    def test_room_detail(self, room):
        self.login('001', '001')
        res = self.client.get('/v1/rooms/1/')
        assert res.status_code == 200
        data = res.json()
        assert data['id'] == 1
        assert data['title'] == 'test001'
        assert len(data['participants']) == 2
        assert data['participants'][0] == 1
        assert data['participants'][1] == 2

    def test_room_detail_non_exist(self, users):
        self.login('001', '001')
        res = self.client.get('/v1/rooms/1/')
        assert res.status_code == 404


@pytest.mark.django_db
class TestMessageView(LoginableTestCase):
    def test_msg_list_without_data(self, room):
        self.login('001', '001')
        res = self.client.get('/v1/rooms/1/messages/')
        assert res.status_code == 200
        data = res.json()
        assert data == []

    def test_msg_list_with_data(self, room, msg):
        self.login('001', '001')
        res = self.client.get('/v1/rooms/1/messages/')
        assert res.status_code == 200
        data = res.json()
        assert len(data) == 1
        msg = data[0]
        assert msg['id'] == 1
        assert msg['sender'] == 1
        assert msg['content'] == 'hello'

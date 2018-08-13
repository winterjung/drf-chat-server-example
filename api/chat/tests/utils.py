import pytest
from rest_framework.test import APIClient


class LoginableTestCase:
    @pytest.fixture(autouse=True)
    def set_up(self, client: APIClient):
        self.client = client

    def login(self, username, password):
        token = self.obtain_token(username, password)
        self.authenticate_with_token(token)

    def obtain_token(self, username, password):
        data = dict(username=username, password=password)
        res = self.client.post('/v1/auth/login', data)
        token = res.data.get('access')
        return token

    def authenticate_with_token(self, token):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

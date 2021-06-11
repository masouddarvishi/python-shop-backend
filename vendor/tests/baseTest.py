from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient

from core.models.user import User


class BaseTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    # create user
    def create_user(self, email='test@gmail.com', password='123456') -> User:
        return get_user_model().objects.create_user(
            email=email,
            password=password,
            name='user_' + email
        )

    # login provided user or create and login user
    def login_user(self, user=None) -> User:
        if user is None:
            user = self.create_user()

        self.client.force_authenticate(user)
        return user;

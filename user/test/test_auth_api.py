from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient


class AuthApiTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='123456'
        )

        self.client.force_authenticate(self.user)

    def test_login_user(self):
        print(reverse('user:auth.login'))
        print('sdf')
        pass

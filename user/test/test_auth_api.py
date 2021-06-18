from django.urls import reverse, path
from django.utils.crypto import get_random_string

from rest_framework import status

from vendor.tests.baseTest import BaseTest

LOGIN_URL = reverse('user:auth-login')
AUTH_USER_URL = reverse('user:auth-user')


class AuthApiTest(BaseTest):

    def test_login_user(self):
        user = self.create_user()
        data = {'email': user.email, 'password': 123456}
        res = self.client.post(LOGIN_URL, data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['email'], user.email)

    def test_get_auth_user(self):
        user = self.login_user()

        res = self.client.get(AUTH_USER_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['email'], user.email)


class AuthFailTest(BaseTest):
    def test_cannot_login_with_wrong_email(self):
        self.create_user()
        payload = {'email': 'uchiha@gmail.com', 'password': '123456'}
        res = self.client.post(LOGIN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cannot_login_with_wrong_password(self):
        self.create_user()
        payload = {'email': 'test@gmail.com', 'password': '1234566'}
        res = self.client.post(LOGIN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_inactive_user_cannot_login(self):
        self.create_user(is_active=False)
        payload = {'email': 'test@gmail.com', 'password': '123456'}
        res = self.client.post(LOGIN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

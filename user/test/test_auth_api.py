from django.urls import reverse, path
from vendor.tests.baseTest import BaseTest


class test:
    @staticmethod
    def a(self):
        pass





class AuthApiTest(BaseTest):
    def test_login_user(self):
        user = self.create_user()
        print(user.__dict__)

    def test_logout_user(self):
        pass

    def test_reset_password_user(self):
        pass

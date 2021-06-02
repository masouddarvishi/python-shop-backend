from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):

        user = self.model(
            email=self.normalize_email(email),
            **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, password, email):
        user = self.model(
            email=self.normalize_email(email),
            is_staff=True,
            is_superuser=True)

        user.set_password(password)
        user.save()

        return user

    def normalize_mobile(self, mobile):
        if mobile is None:
            return None
        d = {'۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4', '۵': '5', '۶': '6',
             '۷': '7', '۸': '8', '۹': '9'}

        for char in mobile:
            if char in d:
                mobile = mobile.replace(char, d[char])

        return mobile


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=30, null=False)
    api_token = models.TextField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'users'

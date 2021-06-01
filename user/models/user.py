from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, mobile, password, **kwargs):
        user = self.model(
            mobile=self.normalize_mobile(mobile),
            **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, password, mobile):
        user = self.model(
            mobile=self.normalize_mobile(mobile),
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
    email = models.EmailField(max_length=255, unique=True, null=True)
    mobile = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=30, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'mobile'

    class Meta:
        db_table = 'users'

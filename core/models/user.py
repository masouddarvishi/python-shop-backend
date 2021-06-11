from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password, name='user_', **kwargs):
        user = self.model(
            email=self.normalize_email(email),
            name='user_' + self.normalize_email(email),
            **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, password, email):
        return self.create_user(
            email=self.normalize_email(email),
            password=password,
            name='admin_',
            is_staff=True,
            is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=30, null=False)
    api_token = models.TextField(max_length=500, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'users'

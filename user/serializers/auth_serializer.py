from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import PBKDF2PasswordHasher

from rest_framework import serializers, exceptions, status

from user.respositories.userReposiory import UserRepository


class AuthSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        trim_whitespace=False,
        required=True,
        min_length=6,
    )

    def validate(self, attrs):
        user_repo = UserRepository()
        user = user_repo.find_via_email(attrs['email'])

        # check if user with requested email exists.
        if user is None:
            raise exceptions.ParseError({'message': 'user not found.'})

        # check if user is active.
        if not user.is_active:
            raise exceptions.PermissionDenied({'message': 'user is not active.'})

        # check user password.
        if not PBKDF2PasswordHasher().verify(attrs['password'], user.password):
            raise exceptions.ParseError({'message': 'user not found.'})

        # get user info and update api_token key
        attrs['user'] = user_repo.update_object(instance=user, api_token=get_random_string(length=256))

        return attrs

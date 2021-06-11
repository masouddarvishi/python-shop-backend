from django.utils.crypto import get_random_string

from rest_framework import serializers, exceptions

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

        if user is None:
            raise serializers.ValidationError({
                'message': 'user not found'
            })

        attrs['user'] = user_repo.update_object(instance=user, api_token=get_random_string(length=256))

        return attrs

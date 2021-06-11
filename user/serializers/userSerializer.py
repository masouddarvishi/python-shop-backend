from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from core.models.user import User
from user.respositories.userReposiory import UserRepository


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = UserRepository().get_model()
        fields = ('email', 'password', 'name', 'api_token', 'is_staff', 'is_active', 'last_login', 'is_superuser')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 6,
                'style': {'input_type': 'password'}
            },
        }

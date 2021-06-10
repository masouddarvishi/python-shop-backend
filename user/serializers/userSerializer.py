from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from core.models.user import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())])
    
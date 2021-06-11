from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse

from user.respositories.userReposiory import UserRepository
from ..serializers.authSerializer import AuthSerializer
from ..serializers.userSerializer import UserSerializer

from django.utils.crypto import get_random_string,pbkdf2


class AuthController(viewsets.ViewSet, TokenAuthentication):
    serializer_class = AuthSerializer

    def login(self, request, *args, **kwargs):
        """ login user by email and password """

        # serialize and validate data
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() is not True:
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        return Response(UserSerializer(serializer.validated_data['user']).data)

    def register(self):
        pass

    def reset_password(self):
        pass

    def auth(self):
        pass

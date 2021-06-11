from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import generics, authentication, permissions

from ..serializers import userSerializer
from vendor.facades.repositories.userReposiory import UserRepository


class UserController(ModelViewSet):
    queryset = UserRepository().get_model().objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    serializer_class = userSerializer.UserSerializer

    # def list(self, request, *args, **kwargs):
    #     users = UserRepository.all()
    #     users = self.serializer_class(data=users)
    #     return Response()

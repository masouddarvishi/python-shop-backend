from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication

from ..serializers import userSerializer
from user.respositories.userReposiory import UserRepository


class UserController(ModelViewSet):
    queryset = UserRepository().get_model().objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    serializer_class = userSerializer.UserSerializer

    # def list(self, request, *args, **kwargs):
    #     users = UserRepository.all()
    #     users = self.serializer_class(data=users)
    #     return Response()

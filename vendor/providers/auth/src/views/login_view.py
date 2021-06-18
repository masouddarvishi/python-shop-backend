from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from user.serializers.userSerializer import UserSerializer


class LoginView:
    @action(methods=['POST'], url_name='login', url_path='login', detail=False, authentication_classes=[], permission_classes=[])
    def login(self, request, *args, **kwargs):
        """ login user by email and password """

        # serialize and validate data
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() is not True:
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        return Response(UserSerializer(serializer.validated_data['user']).data, status.HTTP_200_OK)

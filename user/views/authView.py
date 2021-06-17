from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes, action
from rest_framework.permissions import IsAuthenticated

from ..serializers.authSerializer import AuthSerializer
from ..serializers.userSerializer import UserSerializer


class AuthController(viewsets.ModelViewSet):
    serializer_class = AuthSerializer

    @action(methods=['POST'], url_path='login', detail=False, authentication_classes=(), permission_classes=())
    def login(self, request, *args, **kwargs):
        """ login user by email and password """

        # serialize and validate data
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() is not True:
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        return Response(UserSerializer(serializer.validated_data['user']).data)

    @action(methods=['POST'], url_path='register', detail=False, authentication_classes=(), permission_classes=())
    def register(self, request, *args, **kwargs):
        raise Exception('register founded')
        pass

    @action(methods=['POST'], url_path='register', detail=False, authentication_classes=(), permission_classes=())
    def reset_password(self):
        pass

    @action(methods=['get'], url_path='user', detail=False)
    def auth(self, request):
        raise Exception('route founded')
        return Response(request.headers)

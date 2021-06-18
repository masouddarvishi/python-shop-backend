from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from vendor.providers.auth.src.views.login_view import LoginView

from ..serializers.auth_serializer import AuthSerializer
from ..serializers.userSerializer import UserSerializer


class AuthView(viewsets.ModelViewSet, LoginView):
    serializer_class = AuthSerializer

    @action(methods=['get'], url_path='user', detail=False)
    def user(self, request):
        return Response(UserSerializer(request.user).data)

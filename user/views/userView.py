from rest_framework.viewsets import ModelViewSet
from core.models.user import User


class UserController(ModelViewSet):
    queryset = User.objects.all()

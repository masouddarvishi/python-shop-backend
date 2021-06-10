from rest_framework.permissions import AllowAny
from vendor.reset import RestController
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.decorators import action


class AuthController(viewsets.ModelViewSet):
    def get_serializer_class(self):
        pass

    def login(self, request, *args, **kwargs):
        return JsonResponse({'foo': 'bar'})

        # super(AuthController, self).store(request)
        pass

    def register(self):
        pass

    def reset_password(self):
        pass

    def auth(self):
        pass

from rest_framework import viewsets
from django.http import JsonResponse


class AuthController(viewsets.ViewSet):

    def login(self, request, *args, **kwargs):
        """ login user by email and password """

        return JsonResponse({'foo': 'bar'})

    def register(self):
        pass

    def reset_password(self):
        pass

    def auth(self):
        pass

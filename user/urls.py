from django.urls import path, include
from rest_framework import routers
from .views import authView, userView

app_name = 'user'

router = routers.DefaultRouter()
router.register('users', userView.UserController, basename='users')
router.register('auth', authView.AuthController, basename='auth')

urlpatterns = [
    # user routes
    path('', include(router.urls)),
]

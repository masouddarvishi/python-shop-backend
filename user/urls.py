from django.urls import path, include
from rest_framework import routers
from .views import auth_view, userView

app_name = 'user'

router = routers.DefaultRouter()
router.register('users', userView.UserController, basename='users')
router.register('auth', auth_view.AuthView, basename='auth')

urlpatterns = [
    # user routes
    path('', include(router.urls)),
]

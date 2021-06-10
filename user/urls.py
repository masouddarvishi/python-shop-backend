from django.urls import path, include
from rest_framework import routers
from .views import authView, userView

app_name = 'user'

router = routers.DefaultRouter()
router.register(r'users', userView.UserController, basename='users')

urlpatterns = [
    # auth routes
    path('auth/login', authView.AuthController.as_view({'post': 'login'}), name='auth.login'),
    path('auth/register', authView.AuthController.register, name='auth.register'),

    # user routes
    path('',  include(router.urls)),
]

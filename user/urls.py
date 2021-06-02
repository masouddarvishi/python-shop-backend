from django.urls import path


from .views import AuthView, UserView

app_name = 'user'

urlpatterns = [
    path('auth/login', AuthView.AuthController.login, name='auth.login'),
    path('auth/register', AuthView.AuthController.register, name='auth.register'),
]
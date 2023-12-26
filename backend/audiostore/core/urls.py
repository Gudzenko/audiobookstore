from django.urls import path
from rest_framework.routers import SimpleRouter
from core.user.viewsets import UserViewSet
from core.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
from core.user.views import reset_password


routes = SimpleRouter()

routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

routes.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    *routes.urls,
    path('reset_password/', reset_password, name='reset_password'),
]
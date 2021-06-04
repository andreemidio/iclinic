from django.urls import include, path
from rest_framework import routers

from apps.users import viewsets
from apps.users.viewsets import UserCreateViewSet

app_name = 'users'

router = routers.DefaultRouter()

router.register(r'create-user', UserCreateViewSet, basename='add')

urlpatterns = [
    path(r'', include(router.urls)),
    path('api-token-auth/', viewsets.obtain_auth_token)

]

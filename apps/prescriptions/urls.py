from django.urls import path, include
from rest_framework import routers

from apps.prescriptions.views import hello_world
from apps.prescriptions.viewsets import PostUserPrescriptionsViewSet, ListUserPrescriptionsViewSet

app_name = 'prescriptions'

router = routers.DefaultRouter()

router.register(r'add', PostUserPrescriptionsViewSet, basename='add')
router.register(r'list', ListUserPrescriptionsViewSet, basename='list')

urlpatterns = [
    path(r'', include(router.urls)),
    path('hello', hello_world, name='hello-world'),

]

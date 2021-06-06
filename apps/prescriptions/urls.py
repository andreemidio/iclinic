from django.urls import path, include
from rest_framework import routers

from apps.prescriptions.viewsets import PostUserPrescriptionsViewSet

app_name = 'prescriptions'

router = routers.DefaultRouter()

router.register(r'add', PostUserPrescriptionsViewSet, basename='add')

urlpatterns = [
    path(r'', include(router.urls)),

]

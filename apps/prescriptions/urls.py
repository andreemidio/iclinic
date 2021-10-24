from django.urls import include, path
from rest_framework import routers

from apps.prescriptions.viewsets import (ListUserPrescriptionsViewSet,
                                         PostUserPrescriptionsViewSet)

app_name = 'prescriptions'

router = routers.DefaultRouter()

router.register(r'add', PostUserPrescriptionsViewSet, basename='add')
router.register(r'list', ListUserPrescriptionsViewSet, basename='list')

urlpatterns = [
    path(r'', include(router.urls)),

]

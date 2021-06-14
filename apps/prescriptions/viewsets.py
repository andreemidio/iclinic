# Create your views here.
from rest_framework import mixins, renderers, parsers, permissions, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.prescriptions.models import Prescriptions
from apps.prescriptions.serializers import (
    PrecriptionsSerializers,
    ListPrecriptionsSerializers)


class PostUserPrescriptionsViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Prescriptions.objects.all()
    serializer_class = PrecriptionsSerializers
    renderer_classes = [renderers.StaticHTMLRenderer,  renderers.JSONRenderer]
    parser_classes = (parsers.MultiPartParser, parsers.JSONParser,)
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        data = dict(
            clinic=request.data['clinic']['id'],
            physician=request.data['physician']['id'],
            patient=request.data['patient']['id'],
            text=request.data['text'],
        )

        _prescription = self.queryset.create(**data)

        return Response(request.data, status.HTTP_201_CREATED)


class ListUserPrescriptionsViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Prescriptions.objects.all()
    serializer_class = ListPrecriptionsSerializers
    renderer_classes = [renderers.StaticHTMLRenderer, renderers.JSONRenderer]
    parser_classes = (parsers.MultiPartParser, parsers.JSONParser,)
    permission_classes = (permissions.AllowAny,)

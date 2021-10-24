# Create your views here.
from rest_framework import mixins, parsers, permissions, renderers, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.prescriptions.models import Prescriptions
from apps.prescriptions.serializers import (ListPrecriptionsSerializers,
                                            PrecriptionsSerializers)
from apps.prescriptions.services import RequestEndPoint

request_endpoint = RequestEndPoint()

class PostUserPrescriptionsViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Prescriptions.objects.all()
    serializer_class = PrecriptionsSerializers
    renderer_classes = [renderers.StaticHTMLRenderer, renderers.JSONRenderer]
    parser_classes = (parsers.MultiPartParser, parsers.JSONParser,)
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        if request_endpoint.patients(id=request.data['patient']['id']) == "Not found":
            not_found = dict(
                error=dict(
                    message="patient not found",
                    code="03"
                )

            )
            return Response(not_found, status.HTTP_404_NOT_FOUND)

        if request_endpoint.physicians(id=request.data['physician']['id']) == "Not found":
            not_found = dict(
                error=dict(
                    message="physician not found",
                    code="02"
                )

            )
            return Response(not_found, status.HTTP_404_NOT_FOUND)

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


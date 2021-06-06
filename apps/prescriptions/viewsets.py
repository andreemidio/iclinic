# Create your views here.
from rest_framework import mixins, renderers, parsers, permissions
from rest_framework.viewsets import GenericViewSet

from apps.prescriptions.models import Prescriptions
from apps.prescriptions.serializers import PrecriptionsSerializers


class PostUserPrescriptionsViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Prescriptions.objects.all()
    serializer_class = PrecriptionsSerializers
    renderer_classes = [renderers.StaticHTMLRenderer, renderers.TemplateHTMLRenderer, renderers.JSONRenderer]
    parser_classes = (parsers.MultiPartParser, parsers.JSONParser, parsers.FormParser)
    permission_classes = (permissions.AllowAny,)

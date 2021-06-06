from rest_framework import serializers

from apps.prescriptions.models import Prescriptions


class PrecriptionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prescriptions
        fields = '__all__'

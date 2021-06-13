from rest_framework import serializers

from apps.prescriptions.models import Prescriptions


class ClinicSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class PhysicianSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class PatientSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class PrecriptionsSerializers(serializers.ModelSerializer):
    clinic = ClinicSerializer()
    physician = PhysicianSerializer()
    patient = PatientSerializer()
    text = serializers.CharField()

    class Meta:
        model = Prescriptions
        fields = ['clinic', 'physician', 'patient', 'text']


class ListPrecriptionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prescriptions
        fields = ['id', 'clinic', 'physician', 'patient', 'text']

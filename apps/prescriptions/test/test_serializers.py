import pytest
from rest_framework import exceptions

from apps.prescriptions.models import Prescriptions
from apps.prescriptions.serializers import PrecriptionsSerializers, PatientSerializer, ListPrecriptionsSerializers, \
    ClinicSerializer, PhysicianSerializer


def test_clinic_serializer():
    data = dict(
        id=1
    )

    serializer = ClinicSerializer(data=data)

    assert serializer.is_valid()

    assert serializer.data == data


def test_clinic_serializer_2():
    serializer = ClinicSerializer(data=dict(id='number'))
    with pytest.raises(exceptions.ValidationError) as exc:
        serializer.is_valid(raise_exception=True)

    assert exc.value.detail == {
        'id': [
            exceptions.ErrorDetail('A valid integer is required.', 'invalid')
        ]
    }


def test_physician_serializer():
    data = dict(
        id=1
    )

    serializer = PhysicianSerializer(data=data)

    assert serializer.is_valid()

    assert serializer.data == data


def test_physician_serializer_2():
    serializer = PhysicianSerializer(data=dict(id='number'))
    with pytest.raises(exceptions.ValidationError) as exc:
        serializer.is_valid(raise_exception=True)

    assert exc.value.detail == {
        'id': [
            exceptions.ErrorDetail('A valid integer is required.', 'invalid')
        ]
    }


def test_patient_serializer():
    data = dict(
        id=1
    )

    serializer = PatientSerializer(data=data)

    assert serializer.is_valid()

    assert serializer.data == data


def test_patient_serializer_2():
    serializer = PatientSerializer(data=dict(id='number'))
    with pytest.raises(exceptions.ValidationError) as exc:
        serializer.is_valid(raise_exception=True)

    assert exc.value.detail == {
        'id': [
            exceptions.ErrorDetail('A valid integer is required.', 'invalid')
        ]
    }


def test_prescription_serializer():
    data = {
        "clinic": {
            "id": 0
        },
        "physician": {
            "id": 0
        },
        "patient": {
            "id": 0
        },
        "text": "string"
    }

    serializer = PrecriptionsSerializers(data=data)

    assert serializer.is_valid()

    assert serializer.data == data


# @pytest.mark.django_db(True)
# def test_list_prescription():
#     prescription = Prescriptions.objects.all()
#
#     serializer = ListPrecriptionsSerializers(instance=prescription, many=True)
#
#     assert serializer.data

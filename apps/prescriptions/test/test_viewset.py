import pytest
from rest_framework.test import APIClient

factory = APIClient()


@pytest.mark.django_db
def test_post_prescritions():
    data = {
        "clinic": {
            "id": 1
        },
        "physician": {
            "id": 1
        },
        "patient": {
            "id": 1
        },
        "text": "Dipirona 1x ao dia"
    }

    url = "/api/v1/prescriptions/add/"

    response = factory.post(url, data, format='json')

    assert response.status_code == 201


@pytest.mark.django_db
def test_post_prescriptions_error_physician():
    data = {
        'clinic': {
            'id': 1
        },
        'physician': {
            'id': 150
        },
        'patient': {
            'id': 5

        },
        'text': 'Dipirona 1x ao dia'
    }

    url = "/api/v1/prescriptions/add/"

    response = factory.post(url, data, format='json')

    assert response.status_code == 201


@pytest.mark.django_db
def test_get_prescritions():
    url = "/api/v1/prescriptions/list/"

    response = factory.get(url, format='json')

    assert response.status_code == 200

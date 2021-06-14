import pytest
from django.urls import reverse
from pytest_drf import APIViewTest, Returns200, UsesPostMethod


class TestPrescriptions(
    APIViewTest,
    UsesPostMethod,
    Returns200,
):
    @pytest.fixture
    def url(self):
        return reverse('prescriptions:add')

    def test_returns_prescriptions_add(self, json):
        expected = 'Hello, World!'
        actual = json
        assert expected == actual

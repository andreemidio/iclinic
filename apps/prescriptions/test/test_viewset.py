# import pytest
# from django.urls import reverse
# from pytest_drf import APIViewTest, UsesPostMethod, Returns201
#
#
# class TestPostPrescriptions(
#     APIViewTest,
#     UsesPostMethod,
#     Returns201,
# ):
#     @pytest.fixture
#     def url(self):
#         return reverse('prescriptions:add')
#
#     def test_returns_prescriptions_add(self, json):
#         expected = 'Hello, World!'
#         actual = json
#         assert expected == actual

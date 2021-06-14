# import pytest
# from django.urls import reverse
# from pytest_drf import APIViewTest, Returns200, UsesGetMethod
#
#
# class TestHelloWorld(
#     APIViewTest,
#     UsesGetMethod,
#     Returns200,
# ):
#     @pytest.fixture
#     def url(self):
#         return reverse('prescriptions:hello-world')
#
#     def test_it_returns_hello_world(self, json):
#         expected = 'Hello, World!'
#         actual = json
#         assert expected == actual

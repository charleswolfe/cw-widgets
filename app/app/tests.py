from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

import json


class TestWidgetEndpoints(TestCase):

    def setUp(self):
        self.factory = APIClient()
        self.uri: str = '/widgets/'

    def processResponse(self, incoming):
        return json.loads(incoming.content)

    """
    Test retrieving all of the widgets
    """
    def test_list(self):
        response = self.factory.get(self.uri)
        assert response.status_code == status.HTTP_200_OK

    """
    Test the creation of a widget
    """
    def test_create(self):
        data: dict = {'name': 'Test Widget 1', 'number_of_parts': 2}

        response = self.factory.post(self.uri, data, format='multipart')

        assert response.status_code == status.HTTP_201_CREATED

        response_data = self.processResponse(response)
        self.assertEqual(response_data["name"], data["name"])
        self.assertEqual(
            response_data["number_of_parts"],
            data["number_of_parts"]
            )

    """
    Test retrieving a single widget
    """
    def test_retrieve(self):
        data: dict = {'name': 'Test Widget 1', 'number_of_parts': 2}

        self.factory.post(self.uri, data, format='multipart')
        response = self.factory.get(self.uri + '1')

        assert response.status_code == status.HTTP_200_OK

        response_data = self.processResponse(response)
        self.assertEqual(response_data["name"], data["name"])
        self.assertEqual(
            response_data["number_of_parts"],
            data["number_of_parts"]
        )

    """
    Test updating a widget
    """
    def test_update(self):
        data: dict = {'name': 'Test Widget 1', 'number_of_parts': 2}
        new_data: dict = {'name': 'Test Widget 1', 'number_of_parts': 2}

        self.factory.post(self.uri, data, format='multipart')
        response = self.factory.put(
            self.uri + '1',
            new_data,
            format='multipart'
        )

        assert response.status_code == status.HTTP_200_OK

        response_data = self.processResponse(response)
        self.assertEqual(response_data["name"], new_data["name"])
        self.assertEqual(
            response_data["number_of_parts"],
            new_data["number_of_parts"]
            )

    """
    Test deleting a widget
    """
    def test_delete(self):
        data = {'name': 'Test Widget 1', 'number_of_parts': 2}

        self.factory.post(self.uri, data, format='multipart')
        response = self.factory.delete(self.uri + '1')

        assert response.status_code == status.HTTP_204_NO_CONTENT

        response = self.factory.get(self.uri + '1')

        assert response.status_code == status.HTTP_404_NOT_FOUND

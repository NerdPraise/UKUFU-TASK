from rest_framework import status

from django.shortcuts import reverse

from colonization_project.models import Person
from tests.basetest import BaseTestCase


class PersonTestCase(BaseTestCase):
    fixtures = ["db.yaml"]

    valid_person_data = {"user_one": 1}

    valid_persons_data = {"user_one": 1, "user_two": 2}

    invalid_persons_data = {"user_one": 1, "user_two": 1}

    invalid_data = {}

    def test_when_given_one_person_it_returns_expected_response(self):
        url = reverse("user-get-view")
        person = Person.objects.get(pk=1)

        response = self.client.post(url, self.valid_person_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("username", response.data)
        self.assertIn("age", response.data)
        self.assertIn("fruits", response.data)
        self.assertIn("vegetable", response.data)
        self.assertEqual(response.data["username"], person.username)

    def test_when_given_two_persons_then_it_returns_expected_response(self):
        url = reverse("user-get-view")

        response = self.client.post(url, self.valid_persons_data, format="json")
        self.assertIn("user_one", response.data)
        self.assertIn("user_two", response.data)
        self.assertIn("common_friends", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_when_given_same_two_persons_then_it_returns_error_message(self):
        url = reverse("user-get-view")

        response = self.client.post(url, self.invalid_persons_data, format="json")
        self.assertIn("message", response.data)
        self.assertEqual(response.data["message"], "Specify different users please")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_when_invalid_request_then_it_returns_error_message(self):
        url = reverse("user-get-view")

        response = self.client.post(url, self.invalid_data, format="json")
        self.assertIn("message", response.data)
        self.assertEqual(response.data["message"], "Invalid data")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

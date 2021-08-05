from rest_framework import status

from django.shortcuts import reverse

from colonization_project.models import Company
from tests.basetest import BaseTestCase


class PersonTestCase(BaseTestCase):
    fixtures = ["db.yaml"]

    def test_get_company_by_id(self):
        url = reverse("company-get-view", kwargs={"pk": 1})
        company = Company.objects.get(pk=1)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("employee", response.data)
        self.assertIn("name", response.data)
        self.assertIn("index", response.data)
        self.assertEqual(response.data["name"], company.name)

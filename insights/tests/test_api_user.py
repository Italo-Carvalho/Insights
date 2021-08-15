import json
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from ..models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
import pytest
from .test_api import api_auth_user

pytestmark = pytest.mark.django_db


class UserRegistrationAPIViewTestCase(APITestCase):
    url = reverse("api:user")

    def test_user_invalid_password(self):

        user_data = {
            "email": "test@test.com",
            "password": "",
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(400, response.status_code)

    def test_user_registration(self):

        user_data = {"email": "test@test.com", "password": "passw0rd"}
        response = self.client.post(self.url, user_data)
        self.assertEqual(201, response.status_code)
        self.assertTrue("email" in json.loads(response.content))

    def test_unique_email_validation(self):

        user_data_1 = {"email": "test@test.com", "password": "passw0rd"}
        response = self.client.post(self.url, user_data_1)
        self.assertEqual(201, response.status_code)

        user_data_2 = {"email": "test@test.com", "password": "passw0rd"}
        response = self.client.post(self.url, user_data_2)
        self.assertEqual(400, response.status_code)


class UserJwtLoginTextCase(APITestCase):
    url = reverse("api:token_create")

    def setUp(self):
        self.email = "test@test.com"
        self.password = "passw0rd"
        self.user = CustomUser.objects.create_user(self.email, self.password)

    def test_authentication_without_password(self):
        response = self.client.post(self.url, {"email": self.email})
        self.assertEqual(400, response.status_code)

    def test_authentication_with_wrong_password(self):
        response = self.client.post(
            self.url, {"email": self.email, "password": "passuord"}
        )
        self.assertEqual(401, response.status_code)

    def test_authentication_with_valid_data(self):
        response = self.client.post(
            self.url, {"email": self.email, "password": self.password}
        )
        self.assertEqual(200, response.status_code)
        self.assertTrue("access" in json.loads(response.content))

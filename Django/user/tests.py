from django.test import TestCase
from rest_framework.response import Response
from user.models import User


class UserViewSetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="TestUser",
            password="TestUser",
            email="Test.User@gmail.com",
            is_active=True,
        )

    def test_healthcheck(self):
        url = "/healthcheck/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"Status": "Up"})

    def test_get_user_all(self):
        url = "/api/v1/users/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, Response)
        self.assertIn(self.user.username, response.json()[0]["username"])

    def test_create_user(self):
        url = "/api/v1/users/"
        data = {
            "username": "User",
            "password": "User",
            "email": "User@gmail.com",
            "is_active": True,
        }
        response = self.client.post(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.json()["username"], "User")

    def test_create_user_error(self):
        url = "/api/v1/users/"
        data = {
            "password": "User",
            "email": "User@gmail.com",
            "is_active": True,
        }
        response = self.client.post(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response, Response)
        self.assertEqual(
            response.json(),
            {"username": ["This field is required."]},
        )

    def test_get_user(self):
        url = "/api/v1/users/" + str(self.user.pk) + "/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.json()["username"], self.user.username)

    def test_update_user(self):
        url = "/api/v1/users/" + str(self.user.pk) + "/"
        data = {
            "username": "User1",
            "password": "User",
            "email": "User@gmail.com",
            "is_active": True,
        }
        response = self.client.put(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.json()["username"], "User1")

    def test_update_user_400(self):
        url = "/api/v1/users/" + str(self.user.pk) + "/"
        data = {
            "username": "",
            "password": "User",
            "email": "User@gmail.com",
            "is_active": True,
        }
        response = self.client.put(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response, Response)
        # self.assertEqual(response.json()["username"], "User1")

    def test_partial_update_user(self):
        url = "/api/v1/users/" + str(self.user.pk) + "/"
        data = {
            "username": "User1",
        }
        response = self.client.patch(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.json()["username"], "User1")

    def test_delete_user(self):
        url = "/api/v1/users/" + str(self.user.pk) + "/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())

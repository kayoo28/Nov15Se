from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

User = get_user_model()

class AuthenticationPermissionTests(APITestCase):
    def setUp(self):
        self.normal_user = User.objects.create_user(
            username="normal",
            password="testpass123",
            is_premium=False,
        )
        self.premium_user = User.objects.create_user(
            username="premium",
            password="testpass123",
            is_premium=True,
        )
        self.normal_token = Token.objects.create(user=self.normal_user)
        self.premium_token = Token.objects.create(user=self.premium_user)

    def test_playlist_requires_basic_auth(self):
        response = self.client.get(reverse("playlist-list"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_playlist_with_auth(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.get(reverse("playlist-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_requires_token(self):
        response = self.client.get(reverse("order-list-create"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_order_with_token(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.normal_token.key}"
        )
        response = self.client.get(reverse("order-list-create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cart_without_session_returns_403(self):
        response = self.client.post(
            reverse("cart-create"),
            {"product_name": "Headphones", "quantity": 1},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_non_premium_user_gets_403(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.get(reverse("ticket-list"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_premium_user_gets_200(self):
        self.client.force_authenticate(user=self.premium_user)
        response = self.client.get(reverse("ticket-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_token_generator(self):
        response = self.client.post(
            reverse("generate-token"),
            {"username": "normal", "password": "testpass123"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)

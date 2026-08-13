from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Restaurant


class RestaurantAPITestCase(APITestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name="Spice Garden",
            cuisine="Indian",
            rating=4.5,
        )

    def test_list_returns_200(self):
        response = self.client.get(reverse("restaurant-list-create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_returns_201(self):
        response = self.client.post(
            reverse("restaurant-list-create"),
            {
                "name": "Pizza House",
                "cuisine": "Italian",
                "rating": 4.2,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_returns_200(self):
        response = self.client.get(
            reverse("restaurant-detail", args=[self.restaurant.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_returns_200(self):
        response = self.client.patch(
            reverse("restaurant-detail", args=[self.restaurant.id]),
            {"rating": 4.8},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_returns_204(self):
        response = self.client.delete(
            reverse("restaurant-detail", args=[self.restaurant.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_missing_returns_404(self):
        response = self.client.get(
            reverse("restaurant-detail", args=[99999])
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_rating_returns_400(self):
        response = self.client.post(
            reverse("restaurant-list-create"),
            {
                "name": "Invalid Restaurant",
                "cuisine": "Indian",
                "rating": 6.5,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

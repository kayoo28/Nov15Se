from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Restaurant


class RestaurantViewSetTests(APITestCase):
    def setUp(self):
        Restaurant.objects.create(
            name="Spice Garden",
            cuisine="Indian",
            location="Ahmedabad",
        )
        Restaurant.objects.create(
            name="Roma Kitchen",
            cuisine="Italian",
            location="Surat",
        )
        Restaurant.objects.create(
            name="Curry House",
            cuisine="Indian",
            location="Vadodara",
        )
        Restaurant.objects.create(
            name="Pasta Point",
            cuisine="Italian",
            location="Mumbai",
        )

    def test_router_list_returns_200(self):
        response = self.client.get(reverse("restaurant-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_page_number_has_three_results(self):
        response = self.client.get(reverse("restaurant-list"))
        self.assertEqual(len(response.data["results"]), 3)

    def test_page_two_has_one_result(self):
        response = self.client.get(reverse("restaurant-list") + "?page=2")
        self.assertEqual(len(response.data["results"]), 1)

    def test_ordering_by_name(self):
        response = self.client.get(
            reverse("restaurant-list") + "?ordering=name"
        )
        names = [item["name"] for item in response.data["results"]]
        self.assertEqual(names, sorted(names))

    def test_filter_by_cuisine(self):
        response = self.client.get(
            reverse("restaurant-list") + "?cuisine=Italian"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    def test_limit_offset_endpoint(self):
        response = self.client.get(
            "/api/restaurants/limit-offset/?limit=2&offset=2"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

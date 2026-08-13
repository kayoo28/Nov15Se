from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Doctor


class DoctorAPITestCase(APITestCase):

    def setUp(self):
        self.doctor = Doctor.objects.create(
            name="Dr. Amit Shah",
            specialization="Cardiologist",
            city="Surat",
        )

    def test_list_doctors(self):
        response = self.client.get(reverse("doctor-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_create_doctor(self):
        response = self.client.post(
            reverse("doctor-list"),
            {
                "name": "Dr. Priya Patel",
                "specialization": "Dermatologist",
                "city": "Ahmedabad",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Doctor.objects.count(), 2)

    def test_update_doctor(self):
        response = self.client.patch(
            reverse("doctor-detail", args=[self.doctor.id]),
            {"city": "Vadodara"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.doctor.refresh_from_db()
        self.assertEqual(self.doctor.city, "Vadodara")

    def test_delete_doctor(self):
        response = self.client.delete(
            reverse("doctor-detail", args=[self.doctor.id])
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Doctor.objects.filter(id=self.doctor.id).exists())

    def test_serializer_field_validation(self):
        response = self.client.post(
            reverse("doctor-list"),
            {
                "name": "",
                "specialization": "Cardiologist",
                "city": "Surat",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

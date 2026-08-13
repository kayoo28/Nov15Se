from unittest.mock import patch
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

class Session6Tests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_email_validation(self):
        r = self.client.post("/api/v1/send-email/", {}, format="json")
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(r.data["success"])

    @patch("api.views.send_mailgun_email")
    def test_email(self, mock_send):
        mock_send.return_value = {"id": "queued"}
        r = self.client.post("/api/v1/send-email/", {"email": "user@example.com"}, format="json")
        self.assertEqual(r.status_code, status.HTTP_200_OK)

    @patch("api.views.send_twilio_sms")
    def test_sms(self, mock_send):
        mock_send.return_value = {"sid": "SM123", "status": "queued"}
        r = self.client.post("/api/v1/send-sms/",
                             {"phone": "+919999999999", "message": "Hello"}, format="json")
        self.assertEqual(r.status_code, status.HTTP_200_OK)

    @patch("api.views.create_stripe_payment")
    def test_payment(self, mock_payment):
        mock_payment.return_value = {"id": "pi_test", "status": "requires_payment_method",
                                     "amount": 500, "currency": "usd"}
        r = self.client.post("/api/v1/payment/", {"amount": 500, "currency": "usd"}, format="json")
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)

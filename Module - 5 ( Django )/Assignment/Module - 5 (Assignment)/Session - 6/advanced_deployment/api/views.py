from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import EmailSerializer, SMSSerializer, PaymentSerializer, GoogleLoginSerializer
from .services import send_mailgun_email, send_twilio_sms, create_stripe_payment, get_google_user_info

User = get_user_model()

class SendEmailView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        s = EmailSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        try:
            result = send_mailgun_email(s.validated_data["email"])
        except Exception as exc:
            return Response({"success": False, "error": "Email service failed.", "details": str(exc)},
                            status=status.HTTP_502_BAD_GATEWAY)
        return Response({"success": True, "message": "Welcome email sent successfully.", "mailgun": result})

class SendEmailV2View(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        s = EmailSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        try:
            send_mailgun_email(s.validated_data["email"])
        except Exception as exc:
            return Response({"version": "v2", "success": False, "message": "Could not send welcome email.", "details": str(exc)},
                            status=status.HTTP_502_BAD_GATEWAY)
        return Response({"version": "v2", "success": True, "message": "Welcome email queued."},
                        status=status.HTTP_202_ACCEPTED)

class SendSMSView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        s = SMSSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        try:
            result = send_twilio_sms(s.validated_data["phone"], s.validated_data["message"])
        except Exception as exc:
            return Response({"success": False, "error": "SMS service failed.", "details": str(exc)},
                            status=status.HTTP_502_BAD_GATEWAY)
        return Response({"success": True, "message": "SMS sent successfully.", "twilio": result})

class PaymentView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        s = PaymentSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        try:
            result = create_stripe_payment(s.validated_data["amount"], s.validated_data["currency"])
        except Exception as exc:
            return Response({"success": False, "error": "Payment service failed.", "details": str(exc)},
                            status=status.HTTP_502_BAD_GATEWAY)
        return Response({"success": True, "message": "Payment intent created.", "payment": result},
                        status=status.HTTP_201_CREATED)

class GoogleLoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        s = GoogleLoginSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        try:
            google = get_google_user_info(s.validated_data["access_token"])
        except Exception as exc:
            return Response({"success": False, "error": str(exc)}, status=status.HTTP_401_UNAUTHORIZED)

        email = google["email"]
        user, created = User.objects.get_or_create(
            username=email,
            defaults={
                "email": email,
                "first_name": google.get("given_name", ""),
                "last_name": google.get("family_name", ""),
            },
        )
        refresh = RefreshToken.for_user(user)
        return Response({
            "success": True,
            "created": created,
            "user": {"id": user.id, "email": user.email,
                     "first_name": user.first_name, "last_name": user.last_name},
            "tokens": {"refresh": str(refresh), "access": str(refresh.access_token)},
        })

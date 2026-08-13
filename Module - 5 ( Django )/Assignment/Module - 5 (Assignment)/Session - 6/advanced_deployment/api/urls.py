from django.urls import path
from .views import SendEmailView, SendEmailV2View, SendSMSView, PaymentView, GoogleLoginView

urlpatterns = [
    path("v1/send-email/", SendEmailView.as_view()),
    path("v2/send-email/", SendEmailV2View.as_view()),
    path("v1/send-sms/", SendSMSView.as_view()),
    path("v1/payment/", PaymentView.as_view()),
    path("v1/google-login/", GoogleLoginView.as_view()),
]

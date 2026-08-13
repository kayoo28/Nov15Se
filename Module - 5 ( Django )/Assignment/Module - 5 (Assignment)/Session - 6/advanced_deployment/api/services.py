import os
import requests
import stripe
from twilio.rest import Client

def send_mailgun_email(recipient):
    key = os.getenv("MAILGUN_API_KEY")
    domain = os.getenv("MAILGUN_DOMAIN")
    sender = os.getenv("MAILGUN_FROM_EMAIL")
    if not key or not domain or not sender:
        raise RuntimeError("Mailgun environment variables are not configured.")
    response = requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", key),
        data={"from": sender, "to": [recipient], "subject": "Welcome!",
              "text": "Welcome to our service. Thanks for joining us!"},
        timeout=15,
    )
    response.raise_for_status()
    return response.json()

def send_twilio_sms(phone, message):
    sid = os.getenv("TWILIO_ACCOUNT_SID")
    token = os.getenv("TWILIO_AUTH_TOKEN")
    sender = os.getenv("TWILIO_FROM_NUMBER")
    if not sid or not token or not sender:
        raise RuntimeError("Twilio environment variables are not configured.")
    result = Client(sid, token).messages.create(body=message, from_=sender, to=phone)
    return {"sid": result.sid, "status": result.status}

def create_stripe_payment(amount, currency):
    key = os.getenv("STRIPE_SECRET_KEY")
    if not key:
        raise RuntimeError("STRIPE_SECRET_KEY is not configured.")
    stripe.api_key = key
    intent = stripe.PaymentIntent.create(
        amount=amount, currency=currency.lower(),
        automatic_payment_methods={"enabled": True},
    )
    return {"id": intent.id, "status": intent.status,
            "amount": intent.amount, "currency": intent.currency}

def get_google_user_info(access_token):
    response = requests.get(
        "https://www.googleapis.com/oauth2/v3/userinfo",
        headers={"Authorization": f"Bearer {access_token}"},
        timeout=10,
    )
    if response.status_code != 200:
        raise ValueError("Invalid Google access token.")
    data = response.json()
    if not data.get("email"):
        raise ValueError("Google account did not provide an email address.")
    return data

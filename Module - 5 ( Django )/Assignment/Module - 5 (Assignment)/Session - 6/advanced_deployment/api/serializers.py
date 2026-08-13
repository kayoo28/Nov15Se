from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

class SMSSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=30)
    message = serializers.CharField(max_length=500)

class PaymentSerializer(serializers.Serializer):
    amount = serializers.IntegerField(min_value=1)
    currency = serializers.CharField(max_length=10, default="usd")

class GoogleLoginSerializer(serializers.Serializer):
    access_token = serializers.CharField()

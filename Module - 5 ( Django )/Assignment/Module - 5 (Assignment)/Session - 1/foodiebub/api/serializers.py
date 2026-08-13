from rest_framework import serializers


class RestaurantSerializer(serializers.Serializer):
    # Task 5:
    # Basic Zomato-style Restaurant serializer.

    # AI prompt used:
    # "Write a basic Django REST Framework ModelSerializer class for a
    # Zomato-style Restaurant object with fields name and cuisine.
    # Keep it simple for a beginner assessment and include only the
    # necessary serializer code."

    name = serializers.CharField(max_length=150)

    cuisine = serializers.CharField(max_length=100)

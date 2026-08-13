from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name", "cuisine", "rating"]

    def validate_rating(self, value):
        if value < 0 or value > 5:
            raise serializers.ValidationError(
                "Rating must be between 0 and 5."
            )
        return value

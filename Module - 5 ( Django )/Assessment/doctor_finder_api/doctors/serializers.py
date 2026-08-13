from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["id", "name", "specialization", "city"]

    def validate_name(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError("Name cannot be empty.")

        if value.isdigit():
            raise serializers.ValidationError("Name cannot contain only numbers.")

        return value

    def validate_specialization(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError("Specialization cannot be empty.")

        return value

    def validate_city(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError("City cannot be empty.")

        return value

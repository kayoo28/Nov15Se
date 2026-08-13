from django.db import transaction
from rest_framework import filters, viewsets

from .models import Doctor
from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
 
    queryset = Doctor.objects.all().order_by("id")
    serializer_class = DoctorSerializer

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ["name", "specialization", "city", "id"]
    ordering = ["id"]

    search_fields = ["name", "specialization", "city"]

    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.save()

    def perform_update(self, serializer):
        with transaction.atomic():
            serializer.save()

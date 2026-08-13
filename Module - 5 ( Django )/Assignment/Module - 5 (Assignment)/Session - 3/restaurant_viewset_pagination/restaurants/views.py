from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Restaurant
from .pagination import RestaurantLimitOffsetPagination, RestaurantPageNumberPagination
from .serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all().order_by("id")
    serializer_class = RestaurantSerializer

    # Task 2: PageNumberPagination, 3 records per page.
    pagination_class = RestaurantPageNumberPagination

    # Task 4 + Task 5: ordering and cuisine filtering.
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]

    filterset_fields = ["cuisine"]

    ordering_fields = ["name", "cuisine"]

    ordering = ["name"]


class RestaurantLimitOffsetView(GenericAPIView):
    # Task 3: LimitOffsetPagination demonstration.
    queryset = Restaurant.objects.all().order_by("id")
    serializer_class = RestaurantSerializer
    pagination_class = RestaurantLimitOffsetPagination

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

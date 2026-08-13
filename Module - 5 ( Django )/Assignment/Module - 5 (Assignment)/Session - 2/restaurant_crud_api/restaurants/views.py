from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantListCreateView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    # GET /api/restaurants/ -> 200 OK
    # POST /api/restaurants/ -> 201 Created
    queryset = Restaurant.objects.all().order_by("id")
    serializer_class = RestaurantSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RestaurantDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    # GET -> 200 OK / 404 Not Found
    # PUT/PATCH -> 200 OK / 400 Bad Request / 404 Not Found
    # DELETE -> 204 No Content / 404 Not Found
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

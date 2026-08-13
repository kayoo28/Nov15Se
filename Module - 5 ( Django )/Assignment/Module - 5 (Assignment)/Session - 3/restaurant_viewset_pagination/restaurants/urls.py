from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import RestaurantLimitOffsetView, RestaurantViewSet

router = DefaultRouter()
router.register(r"restaurants", RestaurantViewSet, basename="restaurant")

urlpatterns = [
    path(
        "restaurants/limit-offset/",
        RestaurantLimitOffsetView.as_view(),
        name="restaurant-limit-offset",
    ),
]

urlpatterns += router.urls

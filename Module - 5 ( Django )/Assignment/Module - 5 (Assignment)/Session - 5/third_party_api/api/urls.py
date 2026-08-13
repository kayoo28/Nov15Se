from django.urls import path

from .views import (
    country_info,
    food_location,
    music_weather,
)

urlpatterns = [
    path(
        "music-weather/<str:city>/",
        music_weather,
        name="music-weather",
    ),
    path(
        "food-location/",
        food_location,
        name="food-location",
    ),
    path(
        "country-info/<str:country_name>/",
        country_info,
        name="country-info",
    ),
]

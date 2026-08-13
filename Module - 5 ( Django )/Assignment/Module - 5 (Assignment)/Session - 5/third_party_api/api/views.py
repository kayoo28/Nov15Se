import os

import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
GOOGLE_GEOCODING_URL = "https://maps.googleapis.com/maps/api/geocode/json"
COUNTRIES_URL = "https://restcountries.com/v3.1/name"


@api_view(["GET"])
def music_weather(request, city):
    """
    Task 1:
    Fetch current weather from OpenWeatherMap.
    """

    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        return Response(
            {
                "error": (
                    "OPENWEATHER_API_KEY is not configured. "
                    "Set the environment variable before calling this endpoint."
                )
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    try:
        response = requests.get(
            OPENWEATHER_URL,
            params={
                "q": city,
                "appid": api_key,
                "units": "metric",
            },
            timeout=10,
        )
    except requests.RequestException as exc:
        return Response(
            {"error": f"Weather API request failed: {str(exc)}"},
            status=status.HTTP_502_BAD_GATEWAY,
        )

    if response.status_code == 404:
        return Response(
            {"error": f"City '{city}' was not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    if response.status_code != 200:
        return Response(
            {
                "error": "OpenWeatherMap returned an error.",
                "details": response.text,
            },
            status=status.HTTP_502_BAD_GATEWAY,
        )

    data = response.json()

    return Response(
        {
            "city": data.get("name", city),
            "temperature": data.get("main", {}).get("temp"),
            "description": (
                data.get("weather", [{}])[0].get("description")
            ),
        },
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
def food_location(request):
    """
    Task 2:
    Find restaurant latitude/longitude using Google Maps Geocoding API.

    Query parameter:
    /api/food-location/?restaurant=Pizza+Hut
    """

    restaurant = request.query_params.get("restaurant")

    if not restaurant:
        return Response(
            {"error": "restaurant query parameter is required."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    api_key = os.getenv("GOOGLE_MAPS_API_KEY")

    if not api_key:
        return Response(
            {
                "error": (
                    "GOOGLE_MAPS_API_KEY is not configured. "
                    "Set the environment variable before calling this endpoint."
                )
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    try:
        response = requests.get(
            GOOGLE_GEOCODING_URL,
            params={
                "address": restaurant,
                "key": api_key,
            },
            timeout=10,
        )
    except requests.RequestException as exc:
        return Response(
            {"error": f"Google Maps request failed: {str(exc)}"},
            status=status.HTTP_502_BAD_GATEWAY,
        )

    if response.status_code != 200:
        return Response(
            {
                "error": "Google Maps Geocoding API returned an error.",
                "details": response.text,
            },
            status=status.HTTP_502_BAD_GATEWAY,
        )

    data = response.json()

    if data.get("status") == "ZERO_RESULTS" or not data.get("results"):
        return Response(
            {
                "error": f"Restaurant '{restaurant}' was not found."
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    if data.get("status") != "OK":
        return Response(
            {
                "error": "Google Maps could not geocode the restaurant.",
                "details": data.get("status"),
            },
            status=status.HTTP_502_BAD_GATEWAY,
        )

    location = data["results"][0]["geometry"]["location"]

    return Response(
        {
            "restaurant": restaurant,
            "latitude": location["lat"],
            "longitude": location["lng"],
        },
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
def country_info(request, country_name):
    """
    Task 3:
    Fetch population and capital from REST Countries.
    """

    try:
        response = requests.get(
            f"{COUNTRIES_URL}/{country_name}",
            params={"fields": "name,population,capital"},
            timeout=10,
        )
    except requests.RequestException as exc:
        return Response(
            {"error": f"Country API request failed: {str(exc)}"},
            status=status.HTTP_502_BAD_GATEWAY,
        )

    if response.status_code == 404:
        return Response(
            {
                "error": f"Country '{country_name}' was not found."
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    if response.status_code != 200:
        return Response(
            {
                "error": "REST Countries API returned an error.",
                "details": response.text,
            },
            status=status.HTTP_502_BAD_GATEWAY,
        )

    data = response.json()

    if not data:
        return Response(
            {"error": f"Country '{country_name}' was not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    country = data[0]

    return Response(
        {
            "name": country.get("name", {}).get("common"),
            "population": country.get("population"),
            "capital": (
                country.get("capital", [None])[0]
                if country.get("capital")
                else None
            ),
        },
        status=status.HTTP_200_OK,
    )

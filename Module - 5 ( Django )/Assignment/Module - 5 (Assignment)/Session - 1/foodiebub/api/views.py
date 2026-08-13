from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def hello_spotify(request):
    # Task 3:
    # Return a JSON response when /api/hello_spotify/ is accessed.

    return Response({
        "message": "Hello, Spotify Fans!"
    })




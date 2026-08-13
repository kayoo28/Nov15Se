from rest_framework import generics, status
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .models import CartItem, Order, Playlist, Ticket
from .permissions import IsPremiumUser
from .serializers import (
    CartItemSerializer,
    OrderSerializer,
    PlaylistSerializer,
    TicketSerializer,
)


class PlaylistListView(generics.ListAPIView):
    # Task 1: BasicAuthentication + IsAuthenticated.
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class OrderListCreateView(generics.ListCreateAPIView):
    # Task 2: TokenAuthentication.
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartCreateView(generics.CreateAPIView):
    # Task 3: SessionAuthentication + IsAuthenticated.
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PremiumTicketListView(generics.ListAPIView):
    # Task 4: custom premium-user permission.
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
    ]
    permission_classes = [IsPremiumUser]


class GenerateTokenView(ObtainAuthToken):
    # POST /api/token/ with username and password.
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            token = Token.objects.get(key=response.data["token"])
            return Response(
                {"token": token.key},
                status=status.HTTP_200_OK,
            )

        return response

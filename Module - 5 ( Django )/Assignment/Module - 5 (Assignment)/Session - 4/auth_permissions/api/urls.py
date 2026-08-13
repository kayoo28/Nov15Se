from django.urls import path

from .views import (
    CartCreateView,
    GenerateTokenView,
    OrderListCreateView,
    PlaylistListView,
    PremiumTicketListView,
)

urlpatterns = [
    path("playlists/", PlaylistListView.as_view(), name="playlist-list"),
    path("orders/", OrderListCreateView.as_view(), name="order-list-create"),
    path("cart/", CartCreateView.as_view(), name="cart-create"),
    path("tickets/", PremiumTicketListView.as_view(), name="ticket-list"),
    path("token/", GenerateTokenView.as_view(), name="generate-token"),
]

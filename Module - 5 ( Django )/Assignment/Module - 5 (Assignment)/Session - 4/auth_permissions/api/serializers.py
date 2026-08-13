from rest_framework import serializers

from .models import CartItem, Order, Playlist, Ticket

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ["id", "name", "description"]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "user", "product_name", "quantity"]
        read_only_fields = ["user"]

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["id", "user", "product_name", "quantity"]
        read_only_fields = ["user"]

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["id", "title", "event_name", "price"]

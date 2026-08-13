from django.conf import settings
from django.db import models

class Playlist(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
    )
    product_name = models.CharField(max_length=150)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product_name} - {self.user.username}"

class CartItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cart_items",
    )
    product_name = models.CharField(max_length=150)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product_name} x {self.quantity}"

class Ticket(models.Model):
    title = models.CharField(max_length=150)
    event_name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

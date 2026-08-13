from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    cuisine = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return f"{self.name} - {self.cuisine} ({self.rating})"

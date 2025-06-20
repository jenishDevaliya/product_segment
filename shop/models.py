from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Price in some currency
    size = models.IntegerField()  # Size could be any integer measure

    def __str__(self):
        return f"{self.name} (${self.price}, size={self.size})"

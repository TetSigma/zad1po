from django.db import models

class Product(models.Model):
    nazwa_produktu = models.CharField(max_length=200)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    dostępnosc = models.BooleanField()
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.nazwa_produktu


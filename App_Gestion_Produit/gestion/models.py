from django.db import models
from django.utils import timezone


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_peremption = models.DateField()

    def __str__(self):
        return f"{self.nom} - {self.prix}€"

class Facture(models.Model):
    date = models.DateTimeField(default=timezone.now)
    produits = models.ManyToManyField(Produit)

    def total(self):
        return sum(produit.prix for produit in self.produits.all())

    def __str__(self):
        return f"Facture #{self.id} - {self.date.strftime('%Y-%m-%d %H:%M')}"
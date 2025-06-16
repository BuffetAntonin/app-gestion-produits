from django import forms
from .models import Produit
from .models import Facture

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'prix', 'date_peremption']


class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['produits']
        widgets = {
            'produits': forms.CheckboxSelectMultiple
        }

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['produits']
        widgets = {
            'produits': forms.CheckboxSelectMultiple
        }


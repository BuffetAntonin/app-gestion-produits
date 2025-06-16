from django import forms
from .models import Produit, Facture

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'prix', 'date_peremption']
        widgets = {
            'date_peremption': forms.DateInput(attrs={
                'class': 'form-control datepicker',
                'autocomplete': 'off'
            }),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['produits']
        widgets = {
            'produits': forms.CheckboxSelectMultiple()
        }

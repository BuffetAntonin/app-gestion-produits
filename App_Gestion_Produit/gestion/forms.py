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

# Créer une facture
def creer_facture(request):
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            facture = form.save()
            return redirect('detail_facture', facture.id)
    else:
        form = FactureForm()
    return render(request, 'gestion/facture_form.html', {'form': form})

# Afficher une facture
def detail_facture(request, facture_id):
    facture = get_object_or_404(Facture, pk=facture_id)
    return render(request, 'gestion/facture_detail.html', {'facture': facture})
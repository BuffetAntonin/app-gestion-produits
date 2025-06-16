from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit
from .forms import ProduitForm
from django.core.paginator import Paginator
from .models import Facture
from .forms import FactureForm

# Lister les produits avec pagination
def liste_produits(request):
    produits_list = Produit.objects.all().order_by('nom')
    paginator = Paginator(produits_list, 5)  # 5 produits par page
    page = request.GET.get('page')
    produits = paginator.get_page(page)
    return render(request, 'gestion/liste_produits.html', {'produits': produits})

# Ajouter un produit
def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'gestion/produit_form.html', {'form': form})

# Modifier un produit
def modifier_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'gestion/produit_form.html', {'form': form})

# Supprimer un produit
def supprimer_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    if request.method == 'POST':
        produit.delete()
        return redirect('liste_produits')
    return render(request, 'gestion/produit_confirm_delete.html', {'produit': produit})

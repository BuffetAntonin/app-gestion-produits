from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit
from .forms import ProduitForm
from django.core.paginator import Paginator
from .models import Facture
from .forms import FactureForm
from django.core.paginator import Paginator

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


# Créer une facture
def creer_facture(request):
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            facture = form.save()
            return redirect('detail_facture', facture.id)
    else:
        form = FactureForm()
    return render(request, 'factures/facture_form.html', {'form': form})

# Afficher une facture
def detail_facture(request, facture_id):
    facture = get_object_or_404(Facture, pk=facture_id)
    return render(request, 'factures/facture_detail.html', {'facture': facture})


def liste_factures(request):
    factures = Facture.objects.all().order_by('-date')
    paginator = Paginator(factures, 5)  # 5 factures par page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'factures/liste_factures.html', {'page_obj': page_obj})

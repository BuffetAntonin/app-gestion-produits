from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_produits, name='liste_produits'),
    path('ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('modifier/<int:produit_id>/', views.modifier_produit, name='modifier_produit'),
    path('supprimer/<int:produit_id>/', views.supprimer_produit, name='supprimer_produit'),
]

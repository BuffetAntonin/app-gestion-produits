from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_produits, name='liste_produits'),
    path('ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('modifier/<int:produit_id>/', views.modifier_produit, name='modifier_produit'),
    path('supprimer/<int:produit_id>/', views.supprimer_produit, name='supprimer_produit'),
    path('factures/creer/', views.creer_facture, name='creer_facture'),
    path('factures/<int:facture_id>/', views.detail_facture, name='detail_facture'),
    path('factures/', views.liste_factures, name='liste_factures'),
]

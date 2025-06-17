# 📟 Application de gestion de produits et factures

Ce projet est une application web développée avec **Django** permettant de gérer une liste de produits et de générer des factures associées. Il inclut les fonctionnalités essentielles de création, lecture, mise à jour et suppression (**CRUD**), ainsi que la **pagination** et un affichage détaillé des factures.

---

## 🚀 Fonctionnalités principales

* ✅ Gestion des produits (ajout, modification, suppression)
* ✅ Création de factures à partir de produits
* ✅ Affichage des factures avec pagination
* ✅ Visualisation des détails d'une facture
* ✅ Modification et suppression d'une facture
* ✅ Interface responsive avec Bootstrap

---

## 🛠️ Technologies utilisées

* Python 3.x
* Django
* HTML / CSS (Bootstrap 5)
* SQLite (base de données par défaut de Django)

---

## 📦 Installation

1. **Cloner le dépôt :**

```bash
git clone https://github.com/votre-utilisateur/app-gestion-produits.git
cd app-gestion-produits
```

2. **Créer et activer un environnement virtuel :**

```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

3. **Installer les dépendances :**

```bash
pip install -r requirements.txt
```

4. **Appliquer les migrations :**

```bash
python manage.py migrate
```

5. **Lancer le serveur :**

```bash
python manage.py runserver
```

6. **Accéder à l'application :**

> Ouvrir [http://127.0.0.1:8000](http://127.0.0.1:8000) dans votre navigateur.

---

## 📁 Structure des principales pages

| URL                         | Description                          |
| --------------------------- | ------------------------------------ |
| `/`                         | Liste des produits                   |
| `/ajouter/`                 | Ajouter un produit                   |
| `/modifier/<id>/`           | Modifier un produit                  |
| `/supprimer/<id>/`          | Supprimer un produit                 |
| `/factures/`                | Liste des factures (avec pagination) |
| `/factures/creer/`          | Créer une nouvelle facture           |
| `/factures/<id>/`           | Voir le détail d’une facture         |
| `/factures/<id>/modifier/`  | Modifier une facture                 |
| `/factures/<id>/supprimer/` | Supprimer une facture                |

---

## 🧚‍♂️ Exemple de données (facultatif)

Vous pouvez créer quelques produits manuellement via l’interface pour ensuite générer des factures.

---

## 📌 Auteur

* **\Antonin Buffet**
* Contact : \antonin.buffet.jm@gmail.com

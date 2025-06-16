# Application de gestion de produits et de factures

## 🎯 Objectif
Créer une application web simple avec Django permettant :
- La gestion de produits (CRUD)
- La création de factures à partir des produits
- L'affichage des détails des factures (nombre de produits, total)
- La pagination des listes

## 🛠 Stack utilisée
- Python 3.x
- Django 4.x
- SQLite (par défaut)
- HTML/CSS (avec Bootstrap ou Tailwind)

## 🚀 Installation

```bash
git clone https://github.com/BuffetAntonin/app-gestion-produits.git
cd app-gestion-produits
python -m venv env
source env/bin/activate  # ou `env\Scripts\activate` sous Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

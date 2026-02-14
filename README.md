# 📄 Py PDF Gen

Un script Python 🐍 qui convertit automatiquement des images 📸 en un fichier PDF unique 📑.

## 📖 Description

**Py PDF Gen** est un projet simple permettant de générer un document PDF à partir d’un dossier contenant des images.

✨ Fonctionnalités :

- Support des formats `.png`, `.jpg`, `.jpeg` 🖼️
- Tri automatique des images par ordre alphabétique 🔤
- Création d’un PDF final en une seule commande 📄
- Résultat rapide et pratique pour des scans ou documents 📚

## ⚙️ Installation

### 📥 Cloner le dépôt

```bash
git clone https://github.com/biyayinux/py-pdf-gen.git
```

### 📂 Accéder au dossier

```bash
cd py-pdf-gen
```

### 🐍 Installer les dépendances

```bash
pip install -r requirements.txt
```

## ▶️ Utilisation

### 📂 Ajouter vos images

Placez vos fichiers dans le dossier :

```bash
images_input/
```

### 🚀 Lancer le script

```bash
python src/main.py
```

## ✅ Résultat

Le script génère automatiquement :

📄 `resultat.pdf`

Exemple de message :

```text
PDF créé : resultat.pdf
```

## ⚠️ Problèmes connus

- Le script ignore les fichiers non images ❌
- Aucun PDF n’est généré si le dossier est vide 📭

## 📜 Licence

Vous êtes libre d’utilisation pour apprendre la génération de PDF en Python 🐍.

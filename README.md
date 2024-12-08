# tp_formulaire_api_python

## Description

Une application web basée sur Flask pour soumettre des formulaires et gérer les données via une interface administrateur, avec un design moderne et réactif.

---

## Prérequis

Assurez-vous d’avoir les éléments suivants installés sur votre système :

- Python 3.x
- Environnement virtuel (`venv`)

---

## Instructions d'installation

### Étape 1 : Cloner le dépôt

Clonez ce dépôt sur votre machine locale.

```bash
git clone <url-du-depot>
cd tp_formulaire_api_python
```

### Étape 2 : Créer un environnement virtuel

Créez un environnement virtuel Python pour gérer les dépendances.

```bash
python -m venv env
```

### Étape 3 : Activer l'environnement virtuel

Activez l'environnement virtuel.

- Sur **Windows** :

  ```bash
  .\env\Scripts\activate
  ```

- Sur **macOS/Linux** :
  ```bash
  source env/bin/activate
  ```

### Étape 4 : Installer les dépendances

Installez les bibliothèques Python nécessaires à partir du fichier `requirements.txt`.

```bash
pip install -r requirements.txt
```

### Étape 5 : Configurer la base de données

1. Créez la base de données SQLite (si elle n'existe pas encore) :

   ```bash
   python init_db.py
   ```

2. Optionnellement, ajoutez des données à la base en utilisant des scripts SQL ou via le shell Flask.

### Étape 6 : Exécuter l'application

Lancez l'application Flask.

```bash
python app.py
```

### Étape 7 : Accéder à l'application

Ouvrez votre navigateur et accédez aux pages suivantes :

- Page de formulaire : [http://127.0.0.1:5000/formulaire](http://127.0.0.1:5000/formulaire)
- Panneau administrateur : [http://127.0.0.1:5000/admin](http://127.0.0.1:5000/admin)

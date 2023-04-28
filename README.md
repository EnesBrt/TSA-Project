# Projet TSA (Analyse de Sentiment Textuel)

Le projet TSA est une application Web qui effectue une analyse de sentiment à l'aide d'un réseau neuronal récurrent LSTM bidirectionnel. Les utilisateurs peuvent saisir du texte, et l'application déterminera le sentiment derrière ce texte.

## Table des matières

- [Aperçu du projet](#aperçu-du-projet)
- [DRA snapshots](#dra-snapshots)
- [Templates](#templates)
- [Fichiers](#fichiers)
- [Fonctionnalités](#fonctionnalités)

## Aperçu du projet

Le projet est organisé dans les répertoires et fichiers suivants :

- **Instantanés DRA** : Contient divers captures d'écran et images liées au projet
- **Modèles** : Contient les modèles HTML et les images pour l'application Web
- **Fichiers** : Contient les fichiers principaux pour exécuter l'application Web, entraîner le modèle et gérer la base de données

## DRA snapshots

Ce dossier contient divers captures d'écran et images liées au projet, telles que des visualisations des performances du modèle et des exemples d'entrées/sorties.

## Templates

Ce répertoire contient les modèles HTML et les images pour l'application Web. Il comprend des modèles pour la page d'accueil (`home.html`) et la page de résultats (`result.html`), ainsi que les images associées (`gt.png` et `lk.png`).

## Fichiers

Voici les fichiers du projet :

- `.gitignore` : Spécifie les fichiers et répertoires que Git doit ignorer
- `Procfile` : Utilisé pour déployer l'application sur Heroku
- `Procfile.txt` : Une version texte du Procfile
- `README.md` : Le fichier README du projet
- `Sentiment Analysis RNN Bidirectional lstm.ipynb` : Cahier Jupyter contenant le code d'entraînement et d'évaluation du modèle
- `Sentiment Analysis TSA.py` : Script Python pour l'analyse de sentiment
- `app.py` : Le script principal pour exécuter l'application Web
- `conftest.py` : Fichier de configuration pour les tests
- `database.db` : Fichier de base de données SQLite pour gérer les données
- `database.py` : Script Python pour les opérations de base de données
- `requirements.txt` : Liste des packages requis pour le projet
- `tokenizer.pickle` : Fichier Pickle contenant le tokenizer prétraité

## Fonctionnalités

Le projet TSA traite le texte saisi par l'utilisateur pour déterminer le sentiment à l'aide d'un réseau neuronal récurrent LSTM bidirectionnel entraîné. Les utilisateurs interagissent avec l'application Web pour saisir du texte et recevoir les résultats de l'analyse de sentiment. Le projet inclut une base de données SQLite pour gérer les données, et l'application peut être déployée sur Heroku.

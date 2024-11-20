# Projet : Dashboard Interactif - Évolution de la Surface Forestière

## Description du projet
Ce projet consiste en la création d'un dashboard interactif permettant de visualiser l'évolution de la surface forestière à l'échelle mondiale, continentale et par pays, sur la période 2000-2020. L'objectif principal est de présenter des données sur la déforestation et la gestion des forêts à travers différents graphiques interactifs et une carte dynamique.

## Fonctionnalités principales
- **Visualisation des données** : Le dashboard permet de consulter différentes visualisations de données relatives à la surface forestière.
- **Musique d'ambiance** : La possibilité de jouer de la musique de fond pour rendre l'expérience plus immersive.
- **Carte interactive** : Affichage interactif de la perte de la superficie forestière sur les 20 dernières années avec Folium.
- **Statistiques descriptives** : Des statistiques clés sur les données de surface forestière sont affichées.
- **Graphiques dynamiques** : Des graphiques montrant la répartition de la surface forestière par continent et par pays.
- **Base de données : Terre agricole** : Accès aux données des terres agricoles à partir d'une base de données SQLite intégrée.

## Comment activer l'application
Clonez ce dépôt sur votre machine locale :

```bash
git clone https://github.com/Victor-1901/forest-data-dashboard.git
```

Assurez-vous d'avoir Python et les bibliothèques suivantes installées :

- `streamlit`
- `pandas`
- `folium`
- `streamlit-folium`
- `streamlit-option-menu`

Si ces bibliothèques ne sont pas installées, utilisez la commande suivante pour les installer :

```bash
pip install streamlit pandas folium streamlit-folium streamlit-option-menu
```

Exécutez l'application avec Streamlit :

```bash
streamlit run new_dashboard_forest_utf8.py
```

L'application sera accessible via votre navigateur web à l'adresse par défaut de Streamlit (http://localhost:8501).

## Structure du projet
Le projet est organisé pour respecter l'architecture **MVC** de manière principalement théorique. Voici la structure des dossiers et leur contenu :

- **`new_dashboard_forest_utf8.py`** : Fichier principal à la racine du projet qui sert de point d'entrée à l'application. Il contient toute la logique de l'interface utilisateur via Streamlit.
- **`assets/`** : Contient les ressources telles que les fichiers CSS, les images, les vidéos, et l'audio utilisés par l'application.
  - **`images/`**, **`video/`**, **`audio/`**, **`fichier.css`**
- **`db/`** : Contient la base de données SQLite.
  - **`mon_projet.db`**
- **`src/models/`** : Contient la partie "Modèle" de l'architecture.
  - **`database.py`** : Gestion de la connexion à la base de données.
  - **`session.py`** : Gestion simplifiée des transactions de base de données.
  - **`models.py`** : Définition des entités si nécessaire.
- **`src/views/`** : Contient la partie "Vue" de l'architecture.
  - **`display.py`** : Fonctions pour gérer l'affichage des données et des graphiques dans l'application.

### Architecture MVC
L'architecture **Model-View-Controller (MVC)** est utilisée de manière théorique dans ce projet pour organiser le code :

- **Model** : Gère les données et leur transformation. Le dossier `src/models/` regroupe tout ce qui est relatif à la gestion des données.
- **View** : Gère l'affichage et l'interface utilisateur. Le fichier `new_dashboard_forest_utf8.py` est utilisé pour afficher les données avec Streamlit. Le fichier `display.py` est utilisé pour organiser les éléments de présentation.
- **Controller** : La logique de contrôle est intégrée directement dans `new_dashboard_forest_utf8.py` en tant que fonctions permettant de coordonner la vue et le modèle.

### Limitations
- Le modèle MVC n'est appliqué que de manière théorique. L'application fonctionne principalement en utilisant un fichier principal qui orchestre l'affichage et l'accès aux données.
- Les fichiers et données sont chargés localement, ce qui peut poser des limitations pour une utilisation à grande échelle.

## Auteurs
- Victor - Développeur principal

## Licence
Ce projet est sous licence MIT.






# Projet : Dashboard Interactif - Évolution de la Surface Forestière

## Description du projet
Ce projet consiste en la création d'un dashboard interactif permettant de visualiser l'évolution de la surface forestière à l'échelle mondiale, continentale et par pays, sur la période 2000-2020. L'objectif principal est de présenter des données sur la déforestation et la gestion des forêts à travers différents graphiques interactifs et une carte dynamique.

## Fonctionnalités principales
- **Visualisation des données** : Le dashboard permet de consulter différentes visualisations de données relatives à la surface forestière.
- **Musique d'ambiance** : La possibilité de jouer de la musique de fond pour rendre l'expérience plus immersive.
- **Carte interactive** : Affichage interactif de la perte de la superficie forestière sur les 20 dernières années avec Folium.
- **Statistiques descriptives** : Des statistiques clés sur les données de surface forestière sont affichées.
- **Graphiques dynamiques** : Des graphiques montrant la répartition de la surface forestière par continent et par pays.
- **Base de données : Terre agricole** : Une section permet de visualiser les données sur les terres agricoles stockées dans une base de données SQL.

## Comment activer l'application
Clonez ce dépôt sur votre machine locale :

```bash
git clone https://github.com/Victor-1901/forest-data-dashboard.git

Assurez-vous d'avoir Python et les bibliothèques suivantes installées :

streamlit
pandas
folium
streamlit-folium
streamlit-option-menu

Si ces bibliothèques ne sont pas installées, utilisez la commande suivante pour les installer :
pip install -r requirements.txt


Exécuter l'application avec Streamlit: 

Pour lancer l'application : streamlit run new_dashboard_forest_utf8.py
L'application sera accessible via votre navigateur web à l'adresse par défaut de Streamlit http://localhost:8501.

Structure du projet
Le projet est organisé en plusieurs dossiers pour respecter l'architecture MVC (Model-View-Controller). Voici la structure des dossiers et leur contenu :

assets/ : Contient des ressources nécessaires, comme les fichiers CSS.
db/ : Contient la base de données SQLite (mon_projet.db) utilisée pour stocker les informations sur la surface forestière.
src/ : Contient le fichier principal app.py qui sert de point d'entrée à l'application.
controllers/ (non présent actuellement) : Il est envisagé d'y placer la logique de contrôle, bien que non utilisée directement dans ce projet.
models/ : Contient la gestion des données, tels que le chargement et le traitement des fichiers CSV.
views/ : Contient les fichiers gérant l'affichage des graphiques et des données dans l'application.
Fichiers à la racine du projet :

new_dashboard_forest_utf8.py : Contient tout le code de l'application. Ce fichier est exécuté avec Streamlit.
requirements.txt : Contient la liste des bibliothèques Python nécessaires pour l'exécution du projet.
tests_compatibilite.md : Contient les résultats des tests de compatibilité de l'application sur différents navigateurs.
tests_de_securite.md : Contient les informations sur les tests de sécurité effectués, notamment contre les failles XSS et les injections SQL.
.gitignore : Spécifie les fichiers et dossiers à ignorer lors du commit sur GitHub.
Architecture MVC
L'architecture Model-View-Controller (MVC) est un modèle de conception qui sépare les différentes responsabilités du projet afin de rendre le code plus lisible et maintenable.

Model : Gère les données et leur transformation. Dans ce projet, le modèle gère le chargement et le traitement des fichiers CSV.
View : Gère l'affichage et l'interface utilisateur. Dans ce projet, la vue est gérée par Streamlit, qui permet d'afficher les graphiques, les cartes et les données.
Controller : Coordonne la logique et l'interaction entre les vues et les modèles. Bien que la logique de contrôle soit théorique dans ce projet, elle est définie pour séparer les responsabilités.
Limitations
Modèle MVC : Le modèle MVC est appliqué de manière théorique dans ce projet. L'application fonctionne principalement en se basant sur une architecture plus simple.
Données locales : Les fichiers et données sont chargés localement, ce qui peut poser des limitations pour une utilisation à grande échelle.
Auteurs
Victor - Développeur principal
Licence
Ce projet est sous licence MIT.

Lien vers le dépôt GitHub
Vous pouvez retrouver ce projet sur GitHub en suivant ce lien : forest-data-dashboard







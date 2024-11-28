# **Projet : Dashboard Interactif - Évolution de la Surface Forestière**

## **Description du projet**
Ce projet vise à créer un dashboard interactif permettant de visualiser l'évolution de la surface forestière à l'échelle mondiale, continentale et par pays, sur la période 2000-2020.  
L'objectif est de sensibiliser sur la déforestation et la gestion des forêts grâce à des visualisations interactives et une carte dynamique.

---

## **Fonctionnalités principales**
- **Visualisation des données** : Graphiques interactifs pour explorer les tendances de la surface forestière.
- **Carte interactive** : Suivi de la perte de superficie forestière avec des points interactifs.
- **Statistiques descriptives** : Indicateurs clés sur les surfaces forestières par continent et pays.
- **Musique d'ambiance** : Intégration d'une musique immersive.
- **Base de données SQLite** : Gestion des données agricoles et forestières.

---

## **Accéder à l'application**

### **1. En ligne avec Streamlit Cloud**
L'application est déployée et accessible publiquement :  
🔗 **[Dashboard Interactif - Évolution de la Surface Forestière](https://victor-1901-forest-data-dashbo-new-dashboard-forest-utf8-2qbtei.streamlit.app/)**

---

### **2. En local avec Streamlit**
1. Clonez ce dépôt sur votre machine :
   ```bash
   git clone https://github.com/Victor-1901/forest-data-dashboard.git

2 Installez les dépendances :
pip install -r requirements.txt

3 Lancez l'application Streamlit :
streamlit run new_dashboard_forest_utf8.py

4 Accédez à l'application dans votre navigateur à l'adresse :
 http://localhost:8501.

3. Avec Docker
1 Construisez l'image Docker :
  docker build -t forest-dashboard .

2 Lancez un conteneur Docker :
docker run -p 8501:8501 forest-dashboard

3 Accédez à l'application dans votre navigateur à l'adresse :
http://localhost:8501

Structure du projet
Le projet est structuré pour faciliter son organisation et son déploiement :

Racine du projet :

new_dashboard_forest_utf8.py : Fichier principal contenant toute la logique de l'application.
requirements.txt : Liste des bibliothèques nécessaires.
Dockerfile : Fichier pour créer une image Docker de l'application.
Dossiers :

assets/ : Contient les ressources utilisées par l'application :
fichier.css : Fichier de style pour personnaliser l'interface.
images/ : Images utilisées dans les visualisations et l'interface.
audio/ : Fichiers audio pour la musique d'ambiance.
video/ : Vidéos liées au projet, si nécessaire.
db/ : Contient la base de données SQLite :
mon_projet.db : Base de données des données agricoles et forestières.
src/ : Organisation théorique en MVC :
models/ :
database.py : Gestion des connexions à la base de données.
session.py : Gestion des transactions simplifiées.
models.py : Définition des entités (si nécessaire).
views/ :
display.py : Gestion de l'affichage et des éléments visuels.
Architecture
Le projet suit une organisation inspirée du modèle MVC (Model-View-Controller) :

Model : Gestion des données et de leur transformation (contenu dans src/models/ et db/).
View : Interface utilisateur et visualisation des données (Streamlit via new_dashboard_forest_utf8.py et display.py).
Controller : Logique de l'application, intégrée principalement dans le fichier principal.
Limitations
L'application repose sur un fichier principal (new_dashboard_forest_utf8.py) pour la logique et l'affichage, limitant l'implémentation complète d'une architecture MVC.
Les données sont chargées localement, ce qui peut limiter l'évolutivité pour un usage à grande échelle.
Auteur
Victor - Développeur principal.
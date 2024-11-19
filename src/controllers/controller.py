import streamlit as st
from src.models import data_model  # Importation de la logique de traitement des données
from src.view import display_view  # Importation de la vue pour l'affichage
from streamlit_option_menu import option_menu

def handle_sidebar_menu():
    """
    Gère la sélection du menu dans la barre latérale.
    """
    selected = option_menu("Sommaire Interactif", 
                           ["Problématique", 
                            "Visualisation des données", 
                            "Statistiques descriptives", 
                            "Analyse par pays / année 2023",
                            "Évolution par continent (2000-2020)",
                            "Carte interactive : Perte de surface forestière sur 20 ans",
                            "Vidéo - Déforestation de la forêt amazonienne", 
                            "Conclusion et recommandations"],
                           default_index=0,
                           key="menu_selection")

    # Appel à la fonction de la vue pour afficher le contenu sélectionné
    if selected == "Problématique":
        handle_problematique()
    elif selected == "Visualisation des données":
        handle_visualisation_donnees()
    elif selected == "Statistiques descriptives":
        handle_statistiques_descriptives()
    elif selected == "Analyse par pays / année 2023":
        handle_analyse_par_pays_annee()
    elif selected == "Évolution par continent (2000-2020)":
        handle_evolution_par_continent()
    elif selected == "Carte interactive : Perte de surface forestière sur 20 ans":
        handle_carte_interactive()
    elif selected == "Vidéo - Déforestation de la forêt amazonienne":
        handle_video_deforestation()
    elif selected == "Conclusion et recommandations":
        handle_conclusion_recommandations()

def handle_problematique():
    """
    Gère l'affichage de la section 'Problématique'.
    """
    display_view.display_problematique()

def handle_visualisation_donnees():
    """
    Gère la section 'Visualisation des données'.
    """
    # Charger les données via le modèle
    data = data_model.load_data("C:/Users/victo/nouveau_dataframe_mis_a_jour.csv")

    # Afficher les données dans la vue
    if data is not None:
        display_view.display_data(data)
    else:
        st.error("Les données ne peuvent pas être affichées.")

def handle_statistiques_descriptives():
    """
    Gère l'affichage des statistiques descriptives.
    """
    display_view.display_statistiques()

def handle_analyse_par_pays_annee():
    """
    Gère l'affichage de l'analyse par pays pour l'année 2023.
    """
    display_view.display_analyse_pays_annee()

def handle_evolution_par_continent():
    """
    Gère l'affichage de l'évolution de la superficie forestière par continent de 2000 à 2020.
    """
    display_view.display_evolution_par_continent()

def handle_carte_interactive():
    """
    Gère l'affichage de la carte interactive de la perte de surface forestière.
    """
    display_view.display_carte_interactive()

def handle_video_deforestation():
    """
    Gère l'affichage de la vidéo sur la déforestation.
    """
    display_view.display_video_deforestation()

def handle_conclusion_recommandations():
    """
    Gère l'affichage de la section 'Conclusion et recommandations'.
    """
    display_view.display_conclusion_recommandations()

import streamlit as st
import pandas as pd
import os
from display import show_forest_area_by_continent, show_evolution_by_continent, show_graph, show_map, show_video

# Charger les données (fichier CSV)
def load_data():
    try:
        data = pd.read_csv('C:/Users/victo/nouveau_dataframe_mis_a_jour.csv')  # Met ton chemin ici
        return data
    except Exception as e:
        st.error(f"Erreur lors du chargement des données : {str(e)}")

# Appliquer le CSS
def load_css():
    with open("C:/Users/victo/mon_projet/assets/fichier.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    # Appliquer le fichier CSS
    load_css()

    st.title("Dashboard Interactif : Évolution de la Surface Forestière")

    # Ajouter la musique dans le header, avant le menu interactif
    audio_path = "C:/Users/victo/AMBForst_Foret (ID 0100)_LS.mp3"
    st.audio(audio_path, format="audio/mp3")

    # Menu interactif
    selected = st.sidebar.selectbox(
        "Choisissez une section",
        [
            "Problématique",
            "Visualisation des données",
            "Statistiques descriptives",
            "Analyse par pays / année 2023",
            "Évolution par continent (2000-2020)",
            "Carte interactive : Perte de surface forestière sur 20 ans",
            "Vidéo - Déforestation de la forêt amazonienne",
            "Conclusion et recommandations"
        ]
    )

    # Affichage des sections en fonction de la sélection dans le menu interactif
    if selected == "Problématique":
        st.header("Problématique")
        st.write("Malgré les efforts de conservation, la déforestation continue d'affecter de nombreuses régions. Quelles sont les dynamiques en jeu ?")

    elif selected == "Visualisation des données":
        st.header("Visualisation des Données")
        data = load_data()
        st.dataframe(data)

    elif selected == "Statistiques descriptives":
        st.header("Statistiques descriptives")
        show_forest_area_by_continent()

    elif selected == "Analyse par pays / année 2023":
        st.header("Analyse par pays / année 2023")
        show_graph()

    elif selected == "Évolution par continent (2000-2020)":
        st.header("Évolution par continent (2000-2020)")
        show_evolution_by_continent()

    elif selected == "Carte interactive : Perte de surface forestière sur 20 ans":
        st.header("Carte interactive : Perte de surface forestière sur 20 ans")
        show_map()

    elif selected == "Vidéo - Déforestation de la forêt amazonienne":
        st.header("Vidéo - Déforestation de la forêt amazonienne (1970 - 2024)")
        show_video()

    elif selected == "Conclusion et recommandations":
        st.header("Conclusion et Recommandations")
        st.markdown("""## Conclusion
            L'analyse de l'évolution de la surface forestière révèle des tendances préoccupantes. Malgré les efforts de conservation, la déforestation continue d'affecter de nombreuses régions.
        """)

if __name__ == "__main__":
    main()





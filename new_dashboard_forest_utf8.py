import streamlit as st
import pandas as pd
import base64
import folium
from streamlit_folium import folium_static
from streamlit_option_menu import option_menu
import sqlite3


# Charger le CSS depuis le fichier dans assets
def load_css(css_file_path):
    try:
        with open(css_file_path) as css_file:
            css_content = css_file.read()
            st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Le fichier CSS est introuvable à l'emplacement {css_file_path}.")
    except Exception as e:
        st.error(f"Erreur lors du chargement du CSS : {str(e)}")

load_css("assets/fichier.css")

# Fonction pour charger une image et la convertir en base64
def load_image_as_base64(image_file_path):
    try:
        with open(image_file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        st.error(f"L'image {image_file_path} est introuvable.")
    except Exception as e:
        st.error(f"Erreur lors du chargement de l'image : {str(e)}")

# Utilisation du CSS et de l'image
image_path = 'assets/images/amazonie2.png'  
image_base64 = load_image_as_base64(image_path)

if image_base64:
    st.markdown(f"""
        <style>
            .stApp {{
                background-image: url(data:image/png;base64,{image_base64});
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                color: #FFFFFF;
            }}
            h1 {{
                color: #1B5E20;
                text-shadow: 2px 2px 4px #FFFFFF;
                animation: fadeIn 5s ease-in-out;
            }}
            /* Forcer l'application des styles sur le sous-titre */
            .stSubheader {{
                color: #1B5E20;
                text-shadow: 2px 2px 4px #FFFFFF;
                animation: fadeIn 5s ease-in-out;
            }}
            @keyframes fadeIn {{
                from {{ opacity: 0; }}
                to {{ opacity: 1; }}
            }}
        </style>
    """, unsafe_allow_html=True)

# Titre principal avec un saut de ligne pour plus de clarté
st.title("Dashboard Interactif :")
# Sous-titre avec st.markdown() pour appliquer l'animation et le style
st.markdown("<h2 class='stSubheader'>Évolution de la Surface Forestière</h2>", unsafe_allow_html=True)


# Menu dans la barre latérale
with st.sidebar:
    if 'music_playing' not in st.session_state:
        st.session_state.music_playing = True  # Valeur initiale pour savoir si la musique joue

    # Chemin du fichier audio
    audio_file = "assets/audio/AMBForst_Foret (ID 0100)_LS.mp3"
    
    # Ajout du checkbox pour jouer / arrêter la musique
    if st.checkbox("Jouer la musique", value=st.session_state.music_playing):
        st.session_state.music_playing = True
        try:
            st.audio(audio_file, format='audio/mp3', start_time=0)
        except FileNotFoundError:
            st.error("Le fichier audio est introuvable.")
        except Exception as e:
            st.error(f"Erreur lors de la lecture du fichier audio : {str(e)}")
    else:
        st.session_state.music_playing = False  # Mettre à False pour indiquer que la musique est arrêtée

   # Menu dans la barre latérale
with st.sidebar:
    selected = option_menu("Sommaire Interactif", 
                           ["Problématique",
                            "Visualisation des données",
                            "Statistiques descriptives",
                            "Analyse par pays / année 2023",
                            "Évolution par continent (2000-2020)",
                            "Base de données : Terre agricole",  # Section déplacée avant la carte
                            "Carte interactive : Perte de surface forestière sur 20 ans", # Carte après
                            "Vidéo - Déforestation de la forêt amazonienne",  
                            "Conclusion et recommandations"],
                           default_index=0,
                           key="menu_selection")


# Affichage des sections en fonction de la sélection dans le menu interactif
if selected == "Problématique":
    st.header("Problématique")
    st.write("Malgré les efforts de conservation, la déforestation continue d'affecter de nombreuses régions. Quelles sont les dynamiques en jeu ?")

elif selected == "Visualisation des données":
    st.header("Visualisation des données")
    
    uploaded_file = 'assets/data/nouveau_dataframe_mis_a_jour.csv'  # Chemin du fichier CSV

    try:
        data = pd.read_csv(uploaded_file)
        st.write("Aperçu des données :")
        st.dataframe(data.head())

        st.markdown("<p style='color: #FFFFFF;'>Sélectionnez la colonne à visualiser :</p>", unsafe_allow_html=True)
        col_to_plot = st.selectbox("", data.columns)

        if data[col_to_plot].dtype in ['int64', 'float64']:
            selected_value = st.selectbox("Sélectionnez une valeur :", data[col_to_plot].unique())
            filtered_data = data[data[col_to_plot] == selected_value]
            st.write("Données filtrées :")
            st.dataframe(filtered_data)
        else:
            st.markdown("<p style='color: #FFFFFF;'>La colonne sélectionnée doit être de type numérique.</p>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Le fichier CSV est introuvable.")
    except pd.errors.EmptyDataError:
        st.error("Le fichier est vide.")
    except pd.errors.ParserError:
        st.error("Erreur lors de l'analyse du fichier CSV.")
    except Exception as e:
        st.error(f"Erreur inattendue : {str(e)}")
elif selected == "Statistiques descriptives":
    st.header("Statistiques Descriptives")
    st.markdown("<p style='color: #FFFFFF;'>Choisissez le graphique à afficher :</p>", unsafe_allow_html=True)

    graphique_choisi = st.selectbox("", [
        "Répartition de la Superficie Forestière (%) par Continent en 2023",
        "Répartition de la Superficie Forestière (%) en Europe",
        "Répartition de la Superficie Forestière (%) en Europe avec la France en surbrillance"
    ])

    if graphique_choisi == "Répartition de la Superficie Forestière (%) par Continent en 2023":
        image_path = 'assets/images/superficie_forestiere_boxplot.png'
        try:
            st.image(image_path, caption="Superficie forestière par Continent")
            if st.checkbox("Afficher l'explication du graphique"):
                st.markdown("""
                    Ce graphique en boîte à moustaches présente la répartition de la superficie forestière (%) pour chaque continent en 2023. Il permet de visualiser la couverture forestière entre les continents et fournit une indication de la variabilité et de la densité des forêts dans chaque région.
                    **Éléments du graphique :**
                    - L'axe vertical représente le pourcentage de superficie forestière, mesuré en proportion de la superficie totale de chaque pays.
                    - Chaque boîte représente la distribution des données pour un continent spécifique :
                      - **Ligne médiane** : correspond à la médiane de la superficie forestière pour le continent.
                      - **Quartiles** : la boîte s'étend du premier quartile (Q1) au troisième quartile (Q3), capturant 50 % des valeurs centrales.
                      - **Moustaches** : indiquent les valeurs minimales et maximales excluant les valeurs aberrantes.
                      - **Points isolés** : représentent des valeurs aberrantes, qui se situent en dehors de l'intervalle interquartile.
                    **Analyse des résultats :**
                    - Les continents comme l'Océanie et l'Amérique présentent une plus grande étendue de superficie forestière avec des médianes élevées, suggérant une densité forestière plus significative pour certains pays.
                    - À l'inverse, l'Afrique a une médiane plus basse, reflétant une couverture forestière souvent moindre.
                    - L'Asie et l'Europe montrent des distributions plus resserrées, ce qui indique une répartition plus homogène de la couverture forestière parmi les pays de ces continents.
                    Ce type de visualisation permet de comparer rapidement les niveaux de couverture forestière entre les continents et de mettre en évidence les différences régionales en matière de conservation des forêts.
                """)
        except FileNotFoundError:
            st.error("L'image demandée est introuvable.")
        except Exception as e:
            st.error(f"Erreur lors du chargement de l'image : {str(e)}")

    elif graphique_choisi == "Répartition de la Superficie Forestière (%) en Europe":
        image_path = 'assets/images/Europe foret.png'
        try:
            st.image(image_path, caption="Répartition de la Superficie Forestière en Europe")
            if st.checkbox("Afficher l'explication du graphique"):
                st.markdown("""
                    Ce graphique à points représente la répartition de la superficie forestière (en pourcentage) pour chaque pays européen en 2023. L'axe horizontal présente les différents pays d'Europe, tandis que l'axe vertical indique le pourcentage de superficie forestière par rapport à la superficie totale de chaque pays.
                """)
        except FileNotFoundError:
            st.error("L'image demandée est introuvable.")
        except Exception as e:
            st.error(f"Erreur lors du chargement de l'image : {str(e)}")

    elif graphique_choisi == "Répartition de la Superficie Forestière (%) en Europe avec la France en surbrillance":
        image_path = 'assets/images/_France en surbrillance.png'
        try:
            st.image(image_path, caption="Superficie forestière en France")
            if st.checkbox("Afficher l'explication du graphique"):
                st.markdown("""
                    Ce graphique à points représente la répartition de la superficie forestière (en pourcentage) pour chaque pays européen en 2023, avec la France mise en évidence en rouge pour faciliter la comparaison. L'axe horizontal présente les différents pays d'Europe, tandis que l'axe vertical indique le pourcentage de superficie forestière par rapport à la superficie totale de chaque pays.
                    **Analyse des résultats :**
                    1. **Position de la France** : La France, en surbrillance, se situe à un niveau de couverture forestière autour de 30-40 %, ce qui la place dans une position moyenne parmi les pays européens.
                    2. **Comparaisons internationales** : Certains pays, comme la Suède et la Finlande, affichent des niveaux de couverture forestière très élevés, souvent au-dessus de 60 %, tandis que d'autres, comme le Royaume-Uni et les Pays-Bas, ont des niveaux beaucoup plus bas.
                    3. **Variabilité en Europe** : Ce graphique met en lumière la grande diversité des taux de couverture forestière en Europe, ce qui peut être lié à des facteurs géographiques, climatiques, et politiques différents entre les pays.
                    
                    **Interprétation globale :**  
                    Cette visualisation permet de situer la France par rapport à ses voisins européens en matière de couverture forestière. Elle souligne aussi l’importance de ces données pour orienter les politiques environnementales, notamment dans les pays où la couverture est relativement faible. Les pays à forte couverture forestière, comme la Suède, pourraient servir de modèles pour les autres en termes de gestion forestière.
                """)
        except FileNotFoundError:
            st.error("L'image demandée est introuvable.")
        except Exception as e:
            st.error(f"Erreur lors du chargement de l'image : {str(e)}")
# Section "Analyse par pays / année 2023"
elif selected == "Analyse par pays / année 2023":
    st.header("Analyse par pays / année 2023")
    analyse_graphique_choisi = st.selectbox("Choisissez le graphique à afficher :", [
        "Les 10 Pays avec la Plus Grande Superficie Forestière (%) en 2023",
        "Répartition des Pays Européens avec le Moindre Superficie Forestière en 2023",
        "Corrélation entre la Densité Forestière (%) et les Terres Agricoles (%) en 2023",
        "Corrélation entre le Taux de Natalité et la Densité Forestière (%) en 2023",
        "Corrélation entre le Taux de Population et la Superficie Forestière (%) en 2023"
    ])

    # Affichage du graphique : "Les 10 Pays avec la Plus Grande Superficie Forestière (%) en 2023"
    if analyse_graphique_choisi == "Les 10 Pays avec la Plus Grande Superficie Forestière (%) en 2023":
        image_path = 'assets/images/autre graphique 10 pays.png'
        try:
            st.image(image_path, caption="10 Pays avec le plus de Densité forestière")
            if st.checkbox("Afficher l'explication du graphique"):
                st.markdown("""
                    Ce graphique met en avant les 10 pays ayant le pourcentage de superficie forestière le plus élevé en 2023. Chaque barre représente un pays, et la longueur de la barre indique le pourcentage de couverture forestière par rapport à la superficie totale de ce pays.
                    **Analyse des résultats :**
                    1. **Pays leaders en superficie forestière :** Ce graphique montre que certains pays, notamment les nations d’Europe du Nord, disposent d’une couverture forestière très élevée. Cela peut être dû à des politiques de conservation bien établies, des conditions géographiques favorables et des pratiques d’aménagement du territoire respectueuses de l’environnement.
                    2. **Importance de la forêt dans ces pays :** La forêt joue souvent un rôle crucial dans ces pays, à la fois pour la biodiversité, la régulation climatique et le bien-être de la population locale.
                    3. **Comparaison avec d'autres pays :** Ces chiffres mettent en relief la différence marquée entre ces nations et d'autres pays à couverture forestière plus faible. Cela peut servir de référence pour les pays qui cherchent à augmenter leur superficie forestière.
                    **Interprétation globale :**  
                    Ce graphique illustre l'importance des efforts de conservation et de reforestation dans certains pays et fournit une base de comparaison pour les autres. Ces exemples peuvent guider les politiques environnementales et encourager les pratiques de gestion durable des forêts.
                """)
        except FileNotFoundError:
            st.error("Le fichier image est introuvable.")
        except Exception as e:
            st.error(f"Erreur lors du chargement de l'image : {str(e)}")

    # Affichage du graphique : "Répartition des Pays Européens avec le Moindre Superficie Forestière en 2023"
    elif analyse_graphique_choisi == "Répartition des Pays Européens avec le Moindre Superficie Forestière en 2023":
        image_path = 'assets/images/pays_europeens_faibles_forets.png'
        try:
            st.image(image_path, caption="Pays européens avec faibles forêts")
            if st.checkbox("Afficher l'explication du graphique"):
                st.markdown("""
                    Ce graphique en camembert représente les pays européens ayant la plus faible couverture forestière en 2023. Chaque section du camembert correspond à un pays, et la taille de chaque section indique la proportion de la superficie forestière par rapport à la superficie totale de chaque pays.
                    **Analyse des résultats :**
                    1. **Pays avec une couverture forestière limitée :** Certains pays européens, en particulier ceux ayant une forte densité de population ou une agriculture intensive, affichent des taux de couverture forestière très faibles. Cela peut s'expliquer par un usage intensif des terres à des fins non forestières.
                    2. **Conséquences environnementales :** Une faible couverture forestière peut avoir des impacts significatifs sur la biodiversité et les écosystèmes locaux, ainsi que sur la qualité de l'air et la gestion des ressources en eau.
                    3. **Comparaison avec d'autres pays européens :** En comparant ces pays aux pays européens à forte couverture forestière, on observe des différences notables qui soulignent l'importance des politiques de conservation.
                    **Interprétation globale :**  
                    Ce graphique souligne les défis environnementaux auxquels font face certains pays européens en raison de leur faible couverture forestière. Il met en avant la nécessité d’initiatives de reforestation et de conservation pour rétablir un équilibre écologique dans ces régions.
                """)
        except FileNotFoundError:
            st.error("Le fichier image est introuvable.")
        except Exception as e:
            st.error(f"Erreur lors du chargement de l'image : {str(e)}")

    # Affichage du graphique : "Corrélation entre la Densité Forestière (%) et les Terres Agricoles (%) en 2023"
    elif analyse_graphique_choisi == "Corrélation entre la Densité Forestière (%) et les Terres Agricoles (%) en 2023":
        image_path = 'assets/images/_Terre agricole (%) et la Superficie forestière (%).png'
        try:
            st.image(image_path, caption="Corrélation entre la Densité forestière et les Terres agricoles")
            if st.checkbox("Afficher l'explication du graphique"):
                st.markdown("""
                    Ce graphique de dispersion montre la relation entre le pourcentage de terres agricoles et le pourcentage de superficie forestière pour différents pays en 2023. Chaque point représente un pays, et sa position indique son pourcentage de terres agricoles (axe horizontal) et de superficie forestière (axe vertical).
                    **Analyse des résultats :**
                    1. **Tendance générale :** Le graphique montre une tendance inverse entre les terres agricoles et la superficie forestière. En général, les pays ayant un pourcentage élevé de terres agricoles tendent à avoir une couverture forestière relativement faible, et vice versa.
                    2. **Pays à forte couverture forestière :** Certains pays se situent dans la partie supérieure du graphique, avec une couverture forestière de plus de 70 %, et des pourcentages de terres agricoles relativement bas. Ces pays favorisent probablement la préservation des forêts par rapport à l'expansion des terres agricoles.
                    3. **Pays à forte proportion de terres agricoles :** Les pays avec un pourcentage élevé de terres agricoles (par exemple, au-dessus de 60 %) ont généralement une faible couverture forestière. Cela peut être dû à une utilisation intensive des terres pour l'agriculture, limitant l'espace disponible pour les forêts.
                    **Interprétation globale :**  
                    Ce graphique souligne l'impact de l'agriculture sur la disponibilité des terres forestières. Il révèle une dynamique intéressante entre l'usage agricole et la préservation forestière, suggérant que les pays doivent trouver un équilibre entre ces deux objectifs pour un développement durable.
                """)
        except FileNotFoundError:
            st.error("Le fichier image est introuvable.")
        except Exception as e:
            st.error(f"Erreur lors du chargement de l'image : {str(e)}")

    # Affichage du graphique : "Corrélation entre le Taux de Natalité et la Densité Forestière (%) en 2023"
    elif analyse_graphique_choisi == "Corrélation entre le Taux de Natalité et la Densité Forestière (%) en 2023":
        image_path = 'assets/images/fecondite (1).png'
        try:
            st.image(image_path, caption="Corrélation entre le Taux de natalité et la Densité forestière")
            if st.checkbox("Afficher l'explication du graphique"):
                st.markdown("""
                    Ce graphique de dispersion illustre la relation entre le taux de natalité (axe vertical) et la superficie forestière (axe horizontal) pour différents pays en 2023. Les points sont colorés en fonction du continent auquel chaque pays appartient, permettant de visualiser les différences régionales.
                    **Analyse des résultats :**
                    1. **Tendance générale :** Le graphique ne montre pas de corrélation directe entre le taux de natalité et la superficie forestière, ce qui indique que la densité de couverture forestière ne semble pas être directement liée aux taux de natalité.
                    2. **Différences régionales :** En observant les couleurs, on peut noter certaines variations entre continents. Par exemple, certains pays africains (points verts) présentent des taux de natalité plus élevés avec une couverture forestière variable.
                    3. **Facteurs culturels et géographiques :** Le taux de natalité peut être influencé par des facteurs socio-économiques et culturels propres à chaque région, tandis que la superficie forestière dépend davantage des politiques de conservation et de l'utilisation des terres.
                    **Interprétation globale :**  
                    Ce graphique suggère qu'il existe une diversité dans les relations entre la densité forestière et le taux de natalité d'un pays, influencée par des facteurs régionaux et culturels. Cela souligne la complexité de la gestion des ressources forestières en fonction des dynamiques démographiques.
                """)
        except FileNotFoundError:
            st.error("Le fichier image est introuvable.")
        except Exception as e:
            st.error(f"Erreur lors du chargement de l'image : {str(e)}")

    # Affichage du graphique : "Corrélation entre le Taux de Population et la Superficie Forestière (%) en 2023"
    elif analyse_graphique_choisi == "Corrélation entre le Taux de Population et la Superficie Forestière (%) en 2023":
        image_path = 'assets/images/Relation_Population_Superficie_Forestière (1).png'
        try:
            st.image(image_path, caption="Corrélation entre le Taux de population et la Superficie forestière")
            if st.checkbox("Afficher l'explication du graphique"):
                st.markdown("""
                    Ce graphique de dispersion montre la relation entre la population (axe horizontal) et la superficie forestière (axe vertical) pour différents pays en 2023. Chaque point représente un pays, et sa position illustre le lien entre la densité de population et la couverture forestière.
                    **Analyse des résultats :**
                    1. **Observation principale :** La majorité des points sont concentrés à gauche du graphique, où la population est relativement faible. Cela montre que la plupart des pays avec une couverture forestière significative ont une population modérée à faible.
                    2. **Pays à forte population :** Deux points situés en bas à droite représentent des pays à très forte population avec une faible superficie forestière. Ces pays, très peuplés, ont une couverture forestière limitée, ce qui peut être dû à l’exploitation intensive des terres pour l’habitat et l’agriculture.
                    3. **Absence de corrélation directe :** Le graphique ne révèle pas de corrélation linéaire claire entre la taille de la population et la superficie forestière. Cependant, il souligne une tendance où les pays à plus forte population ont moins de couverture forestière.
                    **Interprétation globale :**  
                    Ce graphique suggère que la taille de la population peut affecter indirectement la superficie forestière, mais sans lien proportionnel strict. Les pays densément peuplés doivent équilibrer les besoins d'urbanisation et de conservation forestière.
                """)
        except FileNotFoundError:
            st.error("Le fichier image est introuvable.")
        except Exception as e:
            st.error(f"Erreur lors du chargement de l'image : {str(e)}")
elif selected == "Évolution par continent (2000-2020)":
    st.header("Évolution de la Surface Forestière par Continent (2000-2020)")
    continent = st.selectbox("Choisissez un continent :", ['Afrique', 'Amérique du Nord', 'Amérique du Sud', 'Asie', 'Europe', 'Océanie'])

    images_path = {
        'Afrique': 'assets/images/afrique chart.png',
        'Amérique du Nord': 'assets/images/AmeriqueNordchart.png',
        'Amérique du Sud': 'assets/images/AmeriqueSud-chart.png',
        'Asie': 'assets/images/Asie-chart.png',
        'Europe': 'assets/images/Europee.png',
        'Océanie': 'assets/images/oceanie-chart.png'
    }

    st.image(images_path[continent], caption=f"Évolution en {continent}")

    # Curseur pour afficher les explications
    show_explanation = st.checkbox("Afficher les explications du graphique", value=False)

    if continent == 'Afrique' and show_explanation:
        st.markdown("""
            ## Couverture forestière moyenne en Afrique (2000-2020)
            Le graphique montre l'évolution de la couverture forestière moyenne en Afrique entre 2000 et 2020. Voici les points clés à retenir :

            **Tendances Générales :**
            - La couverture forestière en Afrique a fluctué entre environ 9,4 % et 11,2 % durant cette période. Ce graphique indique une légère augmentation de la couverture forestière au fil des ans, avec un pic notable.

            **Périodes de Variation :**
            - On observe des pics de couverture forestière, ce qui peut correspondre à des efforts de reforestation ou de conservation dans certains pays africains.
            - Les baisses occasionnelles de la couverture forestière peuvent être attribuées à des facteurs tels que la déforestation illégale et l'expansion agricole.

            **Interprétation :**
            - L'augmentation générale de la couverture forestière au cours de cette période est un indicateur positif, mais la persistance des variations souligne la nécessité de continuer les efforts de conservation.
        """)
    
    elif continent == 'Amérique du Nord' and show_explanation:
        st.markdown("""
            ## Couverture forestière en Amérique du Nord (2000-2020)
            Ce graphique montre la couverture forestière en Amérique du Nord sur la même période. Voici quelques éléments à considérer :

            **Tendances Générales :**
            - La couverture forestière en Amérique du Nord oscille autour de 19 %. Bien que des pics soient visibles, la tendance générale semble montrer une légère amélioration au fil des années.

            **Variabilité :**
            - Les variations peuvent être le résultat de politiques de gestion des forêts, de reforestation ou de déforestation causée par l'urbanisation et les exploitations forestières.

            **Interprétation :**
            - La stabilité de la couverture forestière est encourageante, mais les efforts doivent se poursuivre pour maintenir cette tendance positive et faire face aux défis d'urbanisation.
        """)
    
    elif continent == 'Amérique du Sud' and show_explanation:
        st.markdown("""
            ## Couverture forestière moyenne en Amérique du Sud (2000-2020)
            **Tendances Générales :**
            - La couverture forestière en Amérique du Sud a varié entre 34 % et 36 %, avec des oscillations visibles au fil des ans. Cette dynamique suggère un certain niveau de conservation, mais également des défis.

            **Périodes de Fluctuation :**
            - On observe des pics significatifs, indiquant que des efforts de reforestation ont été entrepris, même si des baisses soulignent les impacts de la déforestation et de l'agriculture intensive.

            **Interprétation :**
            - La fluctuation de la couverture forestière reflète les pressions exercées sur les forêts, mais des initiatives réussies de conservation peuvent aider à atténuer ces effets.
        """)
    
    elif continent == 'Asie' and show_explanation:
        st.markdown("""
            ## Couverture forestière moyenne en Asie (2000-2020)
            **Tendances Générales :**
            - En Asie, la couverture forestière moyenne a également montré une légère augmentation, oscillant entre 16 % et 18,5 % durant cette période.

            **Variabilité :**
            - Les fluctuations observées pourraient être le résultat d'initiatives de reforestation, de gestion des forêts ou de déforestation pour le développement agricole et urbain.

            **Interprétation :**
            - L'augmentation de la couverture forestière est encourageante, mais nécessite une attention continue pour faire face à la pression croissante de la population et du développement.
        """)
    
    elif continent == 'Europe' and show_explanation:
        st.markdown("""
            ## Couverture forestière en Europe (2000-2020)
            **Tendances Générales :**
            - La couverture forestière en Europe oscille autour de 27 %, avec quelques baisses notables, indiquant une variabilité dans la gestion des forêts.

            **Variabilité :**
            - Les baisses peuvent refléter des politiques de gestion des terres ou des périodes de déforestation, tandis que des augmentations pourraient être attribuées à des efforts de reforestation et de conservation.

            **Interprétation :**
            - Bien que la couverture forestière en Europe soit relativement stable, il est essentiel de renforcer les efforts de conservation pour maintenir cette tendance et protéger les forêts.
        """)
    
    elif continent == 'Océanie' and show_explanation:
        st.markdown("""
            ## Couverture forestière moyenne en Océanie (2000-2020)
            **Tendances Générales :**
            - Le graphique montre l'évolution de la couverture forestière moyenne en Océanie entre 2000 et 2020, oscillant autour de 18 % à 19,4 %.
            - Il y a des pics observables, indiquant une amélioration de la couverture forestière à certains moments de cette période.

            **Périodes de Variation :**
            - Les fluctuations peuvent être liées à des initiatives de reforestation ou à des politiques de conservation mises en place dans certains pays de la région.
            - Les baisses temporaires de la couverture forestière peuvent être dues à des phénomènes tels que la déforestation pour des projets d'urbanisation ou d'agriculture.

            **Interprétation :**
            - Bien que la tendance générale montre une couverture forestière relativement stable, la persistance des variations souligne la nécessité de maintenir et de renforcer les efforts de gestion des forêts pour garantir une couverture durable.
        """)

       # Section Base de données : Terre agricole
if selected == "Base de données : Terre agricole":
    st.subheader("Base de données : Terre agricole")

    # Explication pour l'utilisateur
    st.write("""
    Cette section vous présente les données relatives à la superficie des terres agricoles
    pour différents pays. Les données sont récupérées à partir de la base de données SQLite
    utilisée dans l'application.
    """)

    # Connexion à la base de données SQLite avec un gestionnaire de contexte
    with sqlite3.connect('db/mon_projet.db') as conn:
        cursor = conn.cursor()

        # Exécution de la requête SQL pour récupérer toutes les données de la table Terre_Agricole
        cursor.execute('SELECT * FROM Terre_Agricole')

        # Récupération de tous les résultats de la requête
        data = cursor.fetchall()

    # Affichage des données dans l'interface de Streamlit
    st.write(data)  # Affiche les données récupérées de la table Terre_Agricole

# Section "Carte interactive : Perte de surface forestière sur 20 ans"
elif selected == "Carte interactive : Perte de surface forestière sur 20 ans":
    st.header("Carte interactive : Perte de surface forestière sur 20 ans")
    
    # Création de la carte Folium
    m = folium.Map(location=[20, 0], zoom_start=2)  # Centre initial de la carte (monde entier)
    
    # Données de perte/gain de superficie forestière en millions d'hectares par an
    data = {
        'Asie': [2.4, 1.2],
        'Océanie': [0.4, 0.3],
        'Europe': [1.2, 0.2],
        'Amérique du Nord': [-0.1, -0.2],
        'Amérique du Sud': [-5.2, -3.9],
        'Afrique': [-2.6, -3.4],
        'Monde': [-5.2, -4.7]
    }
    
    # Coordonnées géographiques des centres des régions
    coordinates = {
        'Asie': [34, 100],
        'Océanie': [-25, 140],
        'Europe': [50, 10],
        'Amérique du Nord': [40, -100],
        'Amérique du Sud': [-15, -60],
        'Afrique': [0, 20],
        'Monde': [20, 0]
    }

    # Ajout des cercles avec des légendes détaillées pour chaque région
    for region, values in data.items():
        # Cercles pour la période 2000-2010
        folium.CircleMarker(
            location=coordinates[region],
            radius=abs(values[0]) * 10,  # Ajuster le facteur multiplicateur si nécessaire
            color='green' if values[0] >= 0 else 'brown',
            fill=True,
            fill_opacity=0.5,
            popup=(
                f"<b>{region} (2000-2010)</b><br>"
                f"{'Gain' if values[0] >= 0 else 'Perte'} de surface forestière : {abs(values[0])} millions d'hectares par an.<br>"
            )
        ).add_to(m)

        # Cercles pour la période 2010-2020
        folium.CircleMarker(
            location=coordinates[region],
            radius=abs(values[1]) * 10,  # Ajuster le facteur multiplicateur si nécessaire
            color='red' if values[1] < 0 else 'lightgreen',
            fill=True,
            fill_opacity=0.5,
            popup=(
                f"<b>{region} (2010-2020)</b><br>"
                f"{'Perte' if values[1] < 0 else 'Gain'} de surface forestière : {abs(values[1])} millions d'hectares par an.<br>"
            )
        ).add_to(m)

    # Afficher la carte dans l'application Streamlit
    folium_static(m, width=800, height=600)

    # Ajouter une légende dans la barre latérale pour expliquer les couleurs et tailles des cercles
    with st.sidebar:
        st.markdown("""
            <div style="background-color: white; padding: 10px; border: 1px solid black; border-radius: 5px; color: black;">
                <h3 style="margin-top: 0; color: black;">Légende</h3>
                <p><b>Couleurs des cercles :</b></p>
                <ul style="padding-left: 15px; color: black;">
                    <li><span style="color: brown;">●</span> <b>Cercles marron :</b> Perte de surface forestière de 2000 à 2010.</li>
                    <li><span style="color: red;">●</span> <b>Cercles rouges :</b> Perte de surface forestière de 2010 à 2020.</li>
                    <li><span style="color: green;">●</span> <b>Cercles verts :</b> Gain de surface forestière de 2000 à 2010.</li>
                    <li><span style="color: lightgreen;">●</span> <b>Cercles vert clair :</b> Gain de surface forestière de 2010 à 2020.</li>
                </ul>
                <p><b>Taille des cercles :</b> Proportionnelle au nombre d'hectares de forêt perdus ou gagnés.</p>
                <p>Chaque point représente une estimation de la perte ou du gain de surface forestière en millions d'hectares par an.</p>
            </div>
        """, unsafe_allow_html=True)

# Section "Vidéo - Déforestation de la forêt amazonienne"
elif selected == "Vidéo - Déforestation de la forêt amazonienne":
    st.header("Vidéo - Déforestation de la forêt amazonienne (1970 - 2024)")
    
    video_path = "assets/video/Untitled design (1).mp4"
    
    # Vérification si le fichier vidéo existe
    try:
        st.video(video_path)
    except FileNotFoundError:
        st.error("Le fichier vidéo est introuvable. Assurez-vous que le chemin est correct.")
    except Exception as e:
        st.error(f"Erreur lors de la lecture de la vidéo : {str(e)}")
    
    # Ajouter l'explication pour la vidéo
    st.markdown("""
        <p style="color:white;">
            Cette vidéo montre une représentation visuelle de la déforestation de la forêt amazonienne, de 1970 à 2024.<br>
            Vous pouvez observer l'évolution de la perte de surface forestière au fil des décennies.<br>
            <b>Source : Licence Creative Commons (réutilisation autorisée)</b>
        </p>
    """, unsafe_allow_html=True)

# Section "Conclusion et Recommandations"
elif selected == "Conclusion et recommandations":
    st.header("Conclusion et Recommandations")
    st.markdown("""
        ## Conclusion

        L'analyse de l'évolution de la surface forestière révèle des tendances préoccupantes. Malgré les efforts de conservation, la déforestation continue d'affecter de nombreuses régions, principalement en raison de l'expansion de l'agriculture intensive qui remplace les forêts.

        ## Recommandations

        1. **Promotion de pratiques agricoles durables** : Encourager des techniques agricoles comme l'agroforesterie, qui combine la culture avec la préservation des arbres, afin de minimiser l'impact sur les forêts.

        2. **Éducation et sensibilisation** : Sensibiliser les agriculteurs, les entreprises et les gouvernements à l'importance de la couverture forestière pour la biodiversité, le climat et la qualité de vie des populations.

        3. **Renforcement des politiques de conservation** : Mettre en œuvre des réglementations plus strictes pour protéger les forêts et limiter l'expansion de l'agriculture non durable.

        4. **Soutien à la reforestation** : Investir dans des projets de reforestation pour restaurer les zones dégradées, et soutenir des initiatives communautaires qui intègrent la conservation des forêts.

        5. **Collaboration internationale** : Promouvoir la coopération entre les nations pour partager les meilleures pratiques et renforcer les efforts mondiaux contre la déforestation.

        6. **Encourager l'écotourisme** : Développer des initiatives d'écotourisme qui mettent en valeur les forêts et leurs écosystèmes, fournissant ainsi une source de revenus alternative aux communautés locales tout en préservant la biodiversité.
    """)

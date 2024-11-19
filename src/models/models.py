import pandas as pd

def load_data(file_path):
    """
    Charge les données depuis un fichier CSV.
    
    :param file_path: chemin absolu ou relatif du fichier CSV
    :return: DataFrame Pandas si les données sont chargées avec succès, sinon None
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        return None
    except pd.errors.EmptyDataError:
        return None
    except pd.errors.ParserError:
        return None
    except Exception as e:
        raise Exception(f"Erreur inattendue lors du chargement des données : {str(e)}")

def process_data(data):
    """
    Applique les transformations ou traitements nécessaires sur les données.
    Ce peut être la gestion des valeurs manquantes, l'agrégation des données, etc.

    :param data: DataFrame à traiter
    :return: DataFrame traité
    """
    # Exemple de traitement : remplacement des valeurs manquantes par la moyenne
    if data.isnull().sum().any():
        data = data.fillna(data.mean())
    
    # Vous pouvez ajouter plus de traitements ici si nécessaire.
    
    return data

def filter_data_by_column(data, column, value):
    """
    Filtre les données selon une colonne et une valeur données.
    
    :param data: DataFrame à filtrer
    :param column: nom de la colonne à filtrer
    :param value: valeur à rechercher dans la colonne
    :return: DataFrame filtré
    """
    if column in data.columns:
        return data[data[column] == value]
    else:
        raise ValueError(f"Colonne {column} non trouvée dans les données")

def get_summary_statistics(data):
    """
    Retourne les statistiques descriptives des données.
    
    :param data: DataFrame dont les statistiques doivent être calculées
    :return: DataFrame avec les statistiques descriptives
    """
    return data.describe()

def get_correlation(data, col1, col2):
    """
    Calcule la corrélation entre deux colonnes spécifiques du DataFrame.

    :param data: DataFrame contenant les données
    :param col1: première colonne pour la corrélation
    :param col2: deuxième colonne pour la corrélation
    :return: corrélation entre les deux colonnes
    """
    if col1 in data.columns and col2 in data.columns:
        correlation = data[col1].corr(data[col2])
        return correlation
    else:
        raise ValueError(f"Les colonnes {col1} ou {col2} n'existent pas dans les données")

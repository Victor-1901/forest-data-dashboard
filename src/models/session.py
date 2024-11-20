from contextlib import contextmanager
import sqlite3

@contextmanager
def get_session(db_path="db/mon_projet.db"):
    """
    Gestionnaire de contexte pour une session de base de données SQLite.
    Gère l'ouverture, la validation (ou l'annulation) et la fermeture de la connexion.
    :param db_path: Chemin vers la base de données SQLite.
    """
    conn = sqlite3.connect(db_path)
    try:
        yield conn
        conn.commit()  # Valider les changements si tout se passe bien
    except Exception as e:
        conn.rollback()  # Annuler les changements en cas d'erreur
        raise e
    finally:
        conn.close()  # Toujours fermer la connexion

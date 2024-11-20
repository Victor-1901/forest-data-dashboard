import sqlite3

class Database:
    def __init__(self, db_path="db/mon_projet.db") -> None:
        """Initialisation de la connexion à la base de données."""     #sert à faciliter l'accès aux données et à s'assurer que toutes les opérations sur la base de données sont faites de manière sécurisée et organisée
        self.__db = sqlite3.connect(db_path)
    
    def execute(self, query: str, params: tuple = ()):
        """
        Exécute une requête SQL.
        :param query: La requête SQL à exécuter.
        :param params: Les paramètres de la requête, s'il y en a.
        """
        cursor = self.__db.cursor()
        cursor.execute(query, params)
        return cursor

    def commit(self):
        """Valide les changements dans la base de données."""
        self.__db.commit()

    def close(self):
        """Ferme la connexion à la base de données."""
        self.__db.close()

# Exemple d'utilisation
if __name__ == "__main__":
    db = Database()
    try:
        # Création d'une table pour Terre Agricole si elle n'existe pas déjà
        db.execute("""
            CREATE TABLE IF NOT EXISTS Terre_Agricole (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pays VARCHAR,
                superficie_agricole FLOAT
            )
        """)
        db.commit()
    finally:
        db.close()

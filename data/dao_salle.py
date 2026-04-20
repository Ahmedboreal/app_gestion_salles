import json
import mysql.connector


class DataSalle:
    def get_connection(self):
        with open("data/config.json", "r") as fichier:
            config = json.load(fichier)

        connexion = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )

        return connexion

    def insert_salle(self, salle):
        connexion = self.get_connection()
        curseur = connexion.cursor()

        requete = """
        INSERT INTO salle (code, libelle, type, capacite)
        VALUES (%s, %s, %s, %s)
        """

        valeurs = (salle.code, salle.libelle, salle.type, salle.capacite)
        curseur.execute(requete, valeurs)

        connexion.commit()
        curseur.close()
        connexion.close()
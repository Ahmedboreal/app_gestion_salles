from data.dao_salle import DataSalle
from models.salle import Salle

class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()

    def ajouter_salle(self, salle):
        if not salle.code or not salle.libelle or not salle.type or not salle.capacite:
            return False, " Toutes les données de la salle doivent etre renseignées."

        if salle.capacite < 1:
            return False, "La capacité doit etre supérieure ou égale a 1."

        self.dao_salle.insert_salle(salle)
        return True, " salle ajoutée avec succés."
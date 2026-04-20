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

    def modifier_salle(self, salle):
        if not salle.code or not salle.libelle or not salle.type or not salle.capacite:
            return False, " toutes les données de la salle doivent etre renseignées."

        if salle.capacite < 1:
            return False, "la capacité doit etre supérieure ou égale à 1."

        self.dao_salle.update_salle(salle)
        return True, "Salle modifiée avec succès."

    def supprimer_salle(self, code):
        self.dao_salle.delete_salle(code)

    def rechercher_salle(self, code):
        resultat = self.dao_salle.get_salle(code)

        if resultat:
            return Salle(resultat[0], resultat[1], resultat[2], resultat[3])

        return None

    def recuperer_salles(self):
        resultats = self.dao_salle.get_salles()
        liste_salles = []

        for resultat in resultats:
            salle = Salle(resultat[0], resultat[1], resultat[2], resultat[3])
            liste_salles.append(salle)

        return liste_salles
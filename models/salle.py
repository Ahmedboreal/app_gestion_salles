class Salle:
    def __init__(self, code, libelle, type_salle, capacite):
        self.code = code
        self.libelle = libelle
        self.type = type_salle
        self.capacite = capacite

    def afficher_infos(self):
        print("=== Informations de la salle ===")
        print(f"Code : {self.code}")
        print(f"Libellé : {self.libelle}")
        print(f"Type : {self.type}")
        print(f"Capacité : {self.capacite}")
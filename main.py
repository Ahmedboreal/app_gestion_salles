from data.dao_salle import DataSalle
from models.salle import Salle


data_salle = DataSalle()

# Test_connexion
connexion = data_salle.get_connection()
if connexion.is_connected():
    print("Connexion à la base de données réussie.")
connexion.close()

# ajout
salle1 = Salle("B101", "Salle de test", "Classe", 25)
data_salle.insert_salle(salle1)
print("Salle ajoutée.")

# modification
salle1.libelle = "Salle modifiée"
salle1.type = "Laboratoire"
salle1.capacite = 30
data_salle.update_salle(salle1)
print("Salle modifiée.")

# Recherche
salle_trouvee = data_salle.get_salle("B101")
print("Salle trouvée :", salle_trouvee)

# Affichage_de_toutes_les_salles
toutes_les_salles = data_salle.get_salles()
print("Liste des salles :")
for salle in toutes_les_salles:
    print(salle)

# Test_sup
data_salle.delete_salle("B101")
print("Salle supprimée.")
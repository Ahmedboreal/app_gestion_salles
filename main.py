from models.salle import Salle
from services.services_salle import ServiceSalle

service_salle = ServiceSalle()

print("Liste des salles : ")
salles = service_salle.recuperer_salles()
for salle in salles:
    salle.afficher_infos()

nouvelle_salle = Salle("C101", "Salle service", "classe", 20)
succes, message = service_salle.ajouter_salle(nouvelle_salle)
print(message)

nouvelle_salle.libelle = "Salle Service modifiee"
nouvelle_salle.type = "laboratoire"
nouvelle_salle.capacite = 35
succes, message = service_salle.modifier_salle(nouvelle_salle)
print(message)

salle_trouvee = service_salle.rechercher_salle("C101")
if salle_trouvee:
    print("Salle trouvée :")
    salle_trouvee.afficher_infos()
else:
    print(" Salle introuvable.")

service_salle.supprimer_salle("C101")
print("Salle supprimée ")
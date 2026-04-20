import customtkinter as ctk
from services.services_salle import ServiceSalle
from models.salle import Salle


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.service_salle = ServiceSalle()

        self.title("Gestion des salles")
        self.geometry("700x500")

        self.frame_infos = ctk.CTkFrame(self)
        self.frame_infos.pack(pady=10, padx=10, fill="x")

        self.label_code = ctk.CTkLabel(self.frame_infos, text="Code salle :")
        self.label_code.grid(row=0, column=0, padx=10, pady=5)
        self.entry_code = ctk.CTkEntry(self.frame_infos)
        self.entry_code.grid(row=0, column=1, padx=10, pady=5)

        self.label_libelle = ctk.CTkLabel(self.frame_infos, text="Libellé :")
        self.label_libelle.grid(row=1, column=0, padx=10, pady=5)
        self.entry_libelle = ctk.CTkEntry(self.frame_infos)
        self.entry_libelle.grid(row=1, column=1, padx=10, pady=5)

        self.label_type = ctk.CTkLabel(self.frame_infos, text="Type :")
        self.label_type.grid(row=2, column=0, padx=10, pady=5)
        self.entry_type = ctk.CTkEntry(self.frame_infos)
        self.entry_type.grid(row=2, column=1, padx=10, pady=5)

        self.label_capacite = ctk.CTkLabel(self.frame_infos, text="Capacité :")
        self.label_capacite.grid(row=3, column=0, padx=10, pady=5)
        self.entry_capacite = ctk.CTkEntry(self.frame_infos)
        self.entry_capacite.grid(row=3, column=1, padx=10, pady=5)

        self.frame_actions = ctk.CTkFrame(self)
        self.frame_actions.pack(pady=10, padx=10, fill="x")

        self.btn_ajouter = ctk.CTkButton(self.frame_actions, text="Ajouter", command=self.ajouter_salle)
        self.btn_ajouter.grid(row=0, column=0, padx=10, pady=10)

        self.btn_modifier = ctk.CTkButton(self.frame_actions, text="Modifier", command=self.modifier_salle)
        self.btn_modifier.grid(row=0, column=1, padx=10, pady=10)

        self.btn_supprimer = ctk.CTkButton(self.frame_actions, text="Supprimer", command=self.supprimer_salle)
        self.btn_supprimer.grid(row=0, column=2, padx=10, pady=10)

        self.btn_rechercher = ctk.CTkButton(self.frame_actions, text="Rechercher")
        self.btn_rechercher.grid(row=0, column=3, padx=10, pady=10)



    def ajouter_salle(self):
        code = self.entry_code.get()
        libelle = self.entry_libelle.get()
        type_salle = self.entry_type.get()
        capacite = int(self.entry_capacite.get())

        salle = Salle(code, libelle, type_salle, capacite)
        self.service_salle.ajouter_salle(salle)

    def modifier_salle(self):
        code = self.entry_code.get()
        libelle = self.entry_libelle.get()
        type_salle = self.entry_type.get()
        capacite = int(self.entry_capacite.get())

        salle = Salle(code, libelle, type_salle, capacite)
        self.service_salle.modifier_salle(salle)

    def supprimer_salle(self):
        code = self.entry_code.get()
        self.service_salle.supprimer_salle(code)
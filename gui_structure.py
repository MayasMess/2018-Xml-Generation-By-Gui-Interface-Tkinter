from tkinter import *


element_list = {
    "First": {
        "Identifiant_Stable_PDL": "Entry",
        "Rang_QE": {
            "OptionMenu": ["1", "2", "3", "4", "5"]
        },
        "Type_Client": {
            "OptionMenu": ["0", "1"]
        },
        "Type_Relation_Contractuelle": {
            "OptionMenu": ["0", "1", "2", "4"]
        },
        "Evenement_Declencheur": {
            "OptionMenu": ["0", "1", "2", "3", "4", "9"]
        },
        "Numero_Telephone_Depannage_Urgence": "Entry",
        "Facture_Deroutee": {
            "OptionMenu": ["0", "1"]
        },
        "Source_Redressement": {
            "OptionMenu": ["1", "2", "3", "4"]
        },
        "Motif_Redressement": {
            "OptionMenu": ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        },
        "Commentaire_Redressement": "Entry",
        "Date_Theorique_Prochaine_Releve": "Entry",
        "Identifiant_Responsable_Equilibre": "Entry",
        "Code_Tarif": "Entry",
        "Identifiant_Situation": "Entry",
        "Mode_Redressement": {
            "OptionMenu": ["B", "A", "F"]
        },
        "Type_Redressement": {
            "OptionMenu": ["1", "2", "3", "4"]
        },
        "Code_Calcul_Tarif": {
            "OptionMenu": ["00", "11"]
        },
        "Date_Debut_Consommation": "Entry",
        "Date_Fin_Consommation": "Entry",
        "Libelle_Plage_Heures_Creuses": "Entry",
        "Numero_Dossier": "Entry",
        "Reference_Fournisseur": "Entry",
        "Type_Branchement_Provisoire": {
            "OptionMenu": ["92", "96"]
        },
        "Matricule_Compteur": "Entry",
        "Type_Compteur": {
            "OptionMenu": ["CBE", "EMC", "AMM"]
        },
        "Indicateur_De_Periode": {
            "OptionMenu": ["0", "1", "2", "3", "4", "5"]
        },
        "Puissance_Souscrite": "Entry",
        "Type_Historique": {
            "OptionMenu": ["0", "1"]
        },
        "Nombre_Cadrans": {
            "OptionMenu": ["1", "2"]
        },
        "Rang_Cadran": {
            "OptionMenu": ["1", "2"]
        },
        "Nature_Index_Debut": {
            "OptionMenu": ["A", "C", "I", "R"]
        },
        "Processus_Index_Debut": {
            "OptionMenu": ["A", "C", "E", "F", "M", "R", "Z"]
        },
        "Index_Debut_Consommation": "Entry",
        "Origine_Index_Debut": {
            "OptionMenu": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "N", "O", "P", "Q", "R", "S", "T", "U",
                           "V", "W", "X", "Y", "Z"]
        },
        "Indicateur_Passage_A_Zero": {
            "OptionMenu": ["0", "1"]
        },
        "Nature_Index_A_Facturer": {
            "OptionMenu": ["A", "C", "I", "R"]
        },
        "Processus_Index_A_Facturer": {
            "OptionMenu": ["A", "C", "E", "F", "M", "R", "Z"]
        },
        "Index_A_Facturer": "Entry",
        "Origine_Index_A_Facturer": {
            "OptionMenu": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "N", "O", "P", "Q", "R", "S", "T", "U",
                           "V", "W", "X", "Y", "Z"]
        },
        "Consommation_Cadran": "Entry",
        "Historique_Consommation": "Entry"
    },
    "Second": {
        "1": "Entry",
        "2": "Entry",
        "3": "Entry",
        "4": "Entry",
        "5": {
            "OptionMenu": ["1", "2", "3"]
        },
        "hello": "Entry"
    }
}

value_elements = {}
value_flux_elements = {}


def pop_up():
    """
    Open an error pop-up
    :return:
    """
    win = Toplevel()
    win.wm_title("Erreur")

    l = Label(win, text="Veuillez remplir tous les champs")
    l.grid(row=0, column=0)

    b = Button(win, text="Fermer", command=win.destroy)
    b.grid(row=1, column=0)
    print("it's not working bro")



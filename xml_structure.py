#!/usr/bin/env python
# -*- coding: utf-8 -*-


def first_xml(root, value_flux_elements):
    index = root.createElement('Index_C5')
    entete = root.createElement('Entete')
    identifiant_flux = root.createElement('Identifiant_Flux')
    identifiant_flux.appendChild(root.createTextNode('First'))
    libelle_flux = root.createElement('Libelle_Flux')
    libelle_flux.appendChild(
        root.createTextNode(u"Les index (auto relevés, relevés ou établis sur base d'estimation) "
                            u"de début et de fin de consommation par PdL. La valeur de la "
                            u"consommation en KWh d'énergie active par PdL"))
    identifiant_emetteur = root.createElement('Identifiant_Emetteur')
    identifiant_emetteur.appendChild(root.createTextNode('GRD EDF'))
    coordonnees_emetteur = root.createElement('Coordonnees_Emetteur')
    coordonnees_e_ligne1 = root.createElement('Coordonnees_E_Ligne1')
    coordonnees_e_ligne1.appendChild(root.createTextNode('GRD RDF'))
    identifiant_destinataire = root.createElement('Identifiant_Destinataire')
    identifiant_destinataire.appendChild(root.createTextNode('17X100A100R06915'))
    coordonnees_destinataire = root.createElement('Coordonnees_Destinataire')
    coordonnees_d_ligne1 = root.createElement('Coordonnees_D_Ligne1')
    coordonnees_d_ligne1.appendChild(root.createTextNode('17X100A100R06915'))
    date_version_message = root.createElement('Date_Version_Message')
    date_creation = root.createElement('Date_Creation')
    # ----------------------------------------- Non static values ---------------------------------------------- #
    corps_de_fichier_par_pdl = root.createElement('Corps_de_fichier_par_PDL')
    identifiant_stable_pdl = root.createElement('Identifiant_Stable_PDL')
    identifiant_stable_pdl.appendChild(root.createTextNode(value_flux_elements["First"]["Identifiant_Stable_PDL"]))
    rang_qe = root.createElement('Rang_QE')
    rang_qe.appendChild(root.createTextNode(value_flux_elements["First"]["Rang_QE"]))
    type_client = root.createElement('Type_Client')
    type_client.appendChild(root.createTextNode(value_flux_elements["First"]["Type_Client"]))
    type_relation_contractuelle = root.createElement('Type_Relation_Contractuelle')
    type_relation_contractuelle.appendChild(root.createTextNode
                                            (value_flux_elements["First"]["Type_Relation_Contractuelle"]))
    evenement_declencheur = root.createElement('Evenement_Declencheur')
    evenement_declencheur.appendChild(root.createTextNode(value_flux_elements["First"]["Evenement_Declencheur"]))
    numero_telephone_depannage_urgence = root.createElement('Numero_Telephone_Depannage_Urgence')
    numero_telephone_depannage_urgence.appendChild(root.createTextNode
                                                   (value_flux_elements["First"]
                                                    ["Numero_Telephone_Depannage_Urgence"]))
    date_theorique_prochaine_releve = root.createElement('Date_Theorique_Prochaine_Releve')
    date_theorique_prochaine_releve.appendChild(root.createTextNode
                                                (value_flux_elements["First"]["Date_Theorique_Prochaine_Releve"]))
    situation_contrat = root.createElement('Situation_Contrat')
    identifiant_responsable_equilibre = root.createElement('Identifiant_Responsable_Equilibre')
    identifiant_responsable_equilibre.appendChild(
        root.createTextNode(value_flux_elements["First"]["Identifiant_Responsable_Equilibre"]))
    code_tarif = root.createElement('Code_Tarif')
    code_tarif.appendChild(root.createTextNode(value_flux_elements["First"]["Code_Tarif"]))
    identifiant_situation = root.createElement('Identifiant_Situation')
    identifiant_situation.appendChild(root.createTextNode(value_flux_elements["First"]["Identifiant_Situation"]))
    mode_redressement = root.createElement('Mode_Redressement')
    mode_redressement.appendChild(root.createTextNode(value_flux_elements["First"]["Mode_Redressement"]))
    code_calcul_tarif = root.createElement('Code_Calcul_Tarif')
    code_calcul_tarif.appendChild(root.createTextNode(value_flux_elements["First"]["Code_Calcul_Tarif"]))
    date_debut_consommation = root.createElement('Date_Debut_Consommation')
    date_debut_consommation.appendChild(root.createTextNode(value_flux_elements["First"]["Date_Debut_Consommation"]))
    date_fin_consommation = root.createElement('Date_Fin_Consommation')
    date_fin_consommation.appendChild(root.createTextNode(value_flux_elements["First"]["Date_Fin_Consommation"]))
    compteur = root.createElement('Compteur')
    matricule_compteur = root.createElement('Matricule_Compteur')
    matricule_compteur.appendChild(root.createTextNode(value_flux_elements["First"]["Matricule_Compteur"]))
    nombre_cadrans = root.createElement('Nombre_Cadrans')
    nombre_cadrans.appendChild(root.createTextNode(value_flux_elements["First"]["Nombre_Cadrans"]))
    type_compteur = root.createElement('Type_Compteur')
    type_compteur.appendChild(root.createTextNode(value_flux_elements["First"]["Type_Compteur"]))
    periode = root.createElement('Periode')
    indicateur_de_periode = root.createElement('Indicateur_De_Periode')
    indicateur_de_periode.appendChild(root.createTextNode(value_flux_elements["First"]["Indicateur_De_Periode"]))
    puissance_souscrite = root.createElement('Puissance_Souscrite')
    puissance_souscrite.appendChild(root.createTextNode(value_flux_elements["First"]["Puissance_Souscrite"]))
    donnees_cadran = root.createElement('Donnees_Cadran')
    rang_cadran = root.createElement('Rang_Cadran')
    rang_cadran.appendChild(root.createTextNode(value_flux_elements["First"]["Rang_Cadran"]))
    index_debut_consommation = root.createElement('Index_Debut_Consommation')
    index_debut_consommation.appendChild(root.createTextNode
                                         (value_flux_elements["First"]["Index_Debut_Consommation"]))
    indicateur_passage_a_zero = root.createElement('Indicateur_Passage_A_Zero')
    indicateur_passage_a_zero.appendChild(root.createTextNode
                                          (value_flux_elements["First"]["Indicateur_Passage_A_Zero"]))
    nature_index_a_facturer = root.createElement('Nature_Index_A_Facturer')
    nature_index_a_facturer.appendChild(root.createTextNode(value_flux_elements["First"]["Nature_Index_A_Facturer"]))
    processus_index_a_facturer = root.createElement('Processus_Index_A_Facturer')
    processus_index_a_facturer.appendChild(root.createTextNode
                                           (value_flux_elements["First"]["Processus_Index_A_Facturer"]))
    index_a_facturer = root.createElement('Index_A_Facturer')
    index_a_facturer.appendChild(root.createTextNode(value_flux_elements["First"]["Index_A_Facturer"]))
    origine_index_a_facturer = root.createElement('Origine_Index_A_Facturer')
    origine_index_a_facturer.appendChild(root.createTextNode
                                         (value_flux_elements["First"]["Origine_Index_A_Facturer"]))
    consommation_cadran = root.createElement('Consommation_Cadran')
    consommation_cadran.appendChild(root.createTextNode(value_flux_elements["First"]["Consommation_Cadran"]))

    index_elements = [entete, corps_de_fichier_par_pdl]
    entete_elements = [identifiant_flux, libelle_flux, identifiant_emetteur, coordonnees_emetteur,
                       identifiant_destinataire, coordonnees_destinataire, date_version_message, date_creation]
    corps_de_fichier_par_pdl_elements = [identifiant_stable_pdl, rang_qe, type_client, type_relation_contractuelle,
                                         evenement_declencheur, numero_telephone_depannage_urgence,
                                         date_theorique_prochaine_releve, situation_contrat]
    situation_contrat_elements = [identifiant_responsable_equilibre, code_tarif, identifiant_situation,
                                  mode_redressement, code_calcul_tarif, date_debut_consommation,
                                  date_fin_consommation,
                                  compteur]
    compteur_elements = [matricule_compteur, nombre_cadrans, type_compteur, periode]
    periode_elements = [indicateur_de_periode, puissance_souscrite, donnees_cadran]
    donnees_cadran_elements = [rang_cadran, index_debut_consommation, indicateur_passage_a_zero,
                               nature_index_a_facturer, processus_index_a_facturer, index_a_facturer,
                               origine_index_a_facturer, consommation_cadran]

    root.appendChild(index)
    for element in index_elements:
        index.appendChild(element)
    for element in entete_elements:
        entete.appendChild(element)
    coordonnees_emetteur.appendChild(coordonnees_e_ligne1)
    coordonnees_destinataire.appendChild(coordonnees_d_ligne1)
    for element in corps_de_fichier_par_pdl_elements:
        corps_de_fichier_par_pdl.appendChild(element)
    for element in situation_contrat_elements:
        situation_contrat.appendChild(element)
    for element in compteur_elements:
        compteur.appendChild(element)
    for element in periode_elements:
        periode.appendChild(element)
    for element in donnees_cadran_elements:
        donnees_cadran.appendChild(element)


def second_xml(root, value_flux_elements):
    index = root.createElement('Index')
    entete1 = root.createElement('element1')
    entete1.appendChild(root.createTextNode(value_flux_elements["Second"]["1"]))
    entete2 = root.createElement('element2')
    entete2.appendChild(root.createTextNode(value_flux_elements["Second"]["2"]))
    entete3 = root.createElement('element3')
    entete3.appendChild(root.createTextNode(value_flux_elements["Second"]["3"]))
    entete4 = root.createElement('element4')
    entete4.appendChild(root.createTextNode(value_flux_elements["Second"]["4"]))
    entete5 = root.createElement('element5')
    entete5.appendChild(root.createTextNode(value_flux_elements["Second"]["5"]))
    entete6 = root.createElement('element6')
    entete6.appendChild(root.createTextNode(value_flux_elements["Second"]["hello"]))
    root.appendChild(index)
    index_elements = [entete1, entete2, entete3, entete4, entete5, entete6]
    for element in index_elements:
        index.appendChild(element)

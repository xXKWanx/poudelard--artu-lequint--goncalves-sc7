from poudelard.utils.input_utils import demander_choix


def actualiser_points_maison(maisons, nom_maison, points):
    if nom_maison in maisons:
        maisons[nom_maison] += points
    else:
        print(f"Erreur : La maison '{nom_maison}' est introuvable.\n")


def afficher_maison_gagnante(maisons):
    score_maximal = -1
    for nom in maisons:
        if maisons[nom] > score_maximal:
            score_maximal = maisons[nom]

    maisons_gagnantes = []
    for nom in maisons:
        if maisons[nom] == score_maximal:
            maisons_gagnantes.append(nom)

    print("CLASSEMENT ACTUEL DES MAISONS\n")

    nb_gagnants = 0
    for m in maisons_gagnantes:
        nb_gagnants += 1

    if nb_gagnants == 1:
        print(f"La maison gagnante est : {maisons_gagnantes[0]} avec {score_maximal} points !\n")
    elif nb_gagnants > 1:
        noms_egaux = ", ".join(maisons_gagnantes)
        print(f"Égalité ! Les maisons en tête sont : {noms_egaux} avec {score_maximal} points ex æquo.\n")

def repartition_maison(joueur, questions):
    scores_repartition = {"Gryffondor": 0, "Serpentard": 0, "Poufsouffle": 0, "Serdaigle": 0}
    attributs = joueur["Attributs"]

    scores_repartition["Gryffondor"] += attributs["courage"] * 2
    scores_repartition["Serpentard"] += attributs["ambition"] * 2
    scores_repartition["Poufsouffle"] += attributs["loyaute"] * 2
    scores_repartition["Serdaigle"] += attributs["intelligence"] * 2

    for q_data in questions:
        question = q_data[0]
        options = q_data[1]
        maisons_associees = q_data[2]

        print(f"\n{question}")
        choix_valeur = demander_choix("Ton choix", options)

        index_choisi = -1
        actuel = 0
        for opt in options:
            if opt == choix_valeur:
                index_choisi = actuel
            actuel += 1

        maison_choisie = maisons_associees[index_choisi]
        scores_repartition[maison_choisie] += 3

    print("Résumé des scores :")
    for maison in scores_repartition:
        print(f"{maison}: {scores_repartition[maison]} points")

    maison_finale = ""
    score_maximal = -1
    for maison in scores_repartition:
        if scores_repartition[maison] > score_maximal:
            score_maximal = scores_repartition[maison]
            maison_finale = maison

    return maison_finale
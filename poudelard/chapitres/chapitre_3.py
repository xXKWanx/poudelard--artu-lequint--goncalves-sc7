import json
import random


def apprendre_sorts(joueur, chemin_fichier="../data/sorts.json"):
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        data = json.load(fichier)

    sorts_joueur = []
    sorts_utilitaires = []
    sorts_offensifs = []
    sorts_defensifs = []
    for nom_sort in data:
        details = data[nom_sort]
        type_sort = details["type"]
        if type_sort == "Utilitaire":
            sorts_utilitaires.append(nom_sort)
        elif type_sort == "Offensif":
            sorts_offensifs.append(nom_sort)
        elif type_sort == "Défensif":
            sorts_defensifs.append(nom_sort)

    while len(sorts_joueur) < 3:
        index_aleatoire = random.randint(0, len(sorts_utilitaires) - 1)
        sort_choisi = sorts_utilitaires[index_aleatoire]

        if sort_choisi not in sorts_joueur:
            sorts_joueur.append(sort_choisi)

    sorts_joueur.append(random.choice(sorts_defensifs))
    sorts_joueur.append(random.choice(sorts_offensifs))

    joueur["Sortilèges"] = sorts_joueur
    print("Tu commences tes cours de magie à Poudlard...\n")
    for sorts_nom in sorts_joueur:
        details = data[sorts_nom]
        type_sort = details["type"]
        print(f"Tu viens d'apprendre le sortilège : {sorts_nom}{type_sort}\n")
        input("Appuie sur Entrée pour continuer...")

    print("Tu as terminé ton apprentissage de base à Poudlard !\n")
    print("Voici les sortilèges que tu maîtrises désormais :\n")
    for sort_nom in sorts_joueur:
        details = data[sort_nom]
        type_sort = details["type"]
        description = details["description"]
        print(f"{sort_nom} ({type_sort}) : {description}")




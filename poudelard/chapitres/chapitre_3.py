import json
import random
from poudelard.utils.input_utils import load_fichier, demander_texte
from poudelard.univers.maison import actualiser_points_maison
from poudelard.univers.maison import afficher_maison_gagnante
from poudelard.univers.personnage import afficher_personnage


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

def quiz_magie(joueur, chemin_fichier="../data/quiz_magie.json"):
        print("Bienvenue au quiz de magie de Poudlard !")
        print("Réponds correctement aux 4 questions pour faire gagner des points à ta maison.")

        questions_data = load_fichier(chemin_fichier)
        questions_posees = []
        score_total = 0

        while len(questions_posees) < 4:
            question_actuelle = random.choice(questions_data)

            if question_actuelle not in questions_posees:
                questions_posees.append(question_actuelle)

                print(f"{len(questions_posees)}. {question_actuelle['question']}")
                reponse = demander_texte("> ")

                if reponse.lower() == question_actuelle['reponse'].lower():
                    print("Bonne réponse ! +25 points pour ta maison.")
                    score_total += 25
                else:
                    print(f"Mauvaise réponse. La bonne réponse était {question_actuelle['reponse']}")

        print(f"Score obtenu : {score_total} points")
        return score_total

def lancer_chapitre_3(personnage, maisons):
    print("==================================================")
    print("              CHAPTER 3: COURS & QUIZ MAGIQUE     ")
    print("==================================================")


    print("\n--- Leçon de Sortilèges ---")
    apprendre_sorts(personnage)
    print("\n--- Quiz de Magie ---")
    score_quiz = quiz_magie(personnage)
    nom_maison_joueur = personnage["Maison"]
    actualiser_points_maison(maisons, nom_maison_joueur, score_quiz)
    print("\n--- Classement Actuel des Maisons ---")
    afficher_maison_gagnante(maisons)
    print("\n--- Profil du Joueur après Chapitre 3 ---")
    afficher_personnage(personnage)
    print("\n<<< Fin du Chapitre 3 ! Préparez-vous pour le grand événement de fin d'année... >>>\n")





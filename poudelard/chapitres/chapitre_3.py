import random
from poudelard.utils.input_utils import load_fichier, demander_texte
from poudelard.univers.maison import actualiser_points_maison
from poudelard.univers.maison import afficher_maison_gagnante
from poudelard.univers.personnage import afficher_personnage

def apprendre_sorts(joueur, chemin_fichier="data/sorts.json"):
    tous_les_sorts = load_fichier(chemin_fichier)

    sorts_appris = []
    quotas = {"Offensif": 1, "Défensif": 1, "Utilitaire": 3}
    compteurs = {"Offensif": 0, "Défensif": 0, "Utilitaire": 0}

    print("Tu commences tes cours de magie à Poudlard...\n")

    while compteurs["Offensif"] < quotas["Offensif"] or compteurs["Défensif"] < quotas["Défensif"] or compteurs["Utilitaire"] < quotas["Utilitaire"]:

        sort = random.choice(tous_les_sorts)
        nom = sort["nom"]
        type_sort = sort["type"]

        if compteurs[type_sort] < quotas[type_sort] and nom not in joueur["Sortilèges"]:
            joueur["Sortilèges"].append(nom)
            compteurs[type_sort] += 1
            sorts_appris.append(sort)
            print(f"Tu viens d'apprendre le sortilège: {nom} ({type_sort})\n")
            demander_texte("Appuie sur Entrée pour continuer...")

    print("Tu as terminé ton apprentissage de base à Poudlard !\n")
    print("Voici les sortilèges que tu maîtrises désormais :\n")

    for s in sorts_appris:
        print(f"{s['nom']} ({s['type']}) : {s['description']}")

def quiz_magie(joueur, chemin_fichier="data/quiz_magie.json"):
        print("Bienvenue au quiz de magie de Poudlard !\n")
        print("Réponds correctement aux 4 questions pour faire gagner des points à ta maison.\n")

        questions_data = load_fichier(chemin_fichier)
        questions_posees = []
        score_total = 0

        nb_questions = 0
        while nb_questions < 4:
            question_actuelle = random.choice(questions_data)
            if question_actuelle not in questions_posees:
                questions_posees.append(question_actuelle)
                nb_questions += 1  # Incrémentation manuelle

                print(f"{nb_questions}. {question_actuelle['question']}")
                reponse = demander_texte("> ")

                if reponse.lower() == question_actuelle['reponse'].lower():
                    print("Bonne réponse ! +25 points pour ta maison.\n")
                    score_total += 25
                else:
                    print(f"Mauvaise réponse. La bonne réponse était {question_actuelle['reponse']}\n")

        print(f"Score obtenu : {score_total} points")
        return score_total

def lancer_chapitre_3(personnage, maisons):
    print("==================================================\n")
    print("          CHAPTER 3: COURS & QUIZ MAGIQUE         \n")
    print("==================================================\n")


    print("--- Leçon de Sortilèges ---\n")
    apprendre_sorts(personnage, "data/sorts.json")
    print("--- Quiz de Magie ---")
    score_quiz = quiz_magie(personnage, "data/quiz_magie.json")
    nom_maison_joueur = personnage["Maison"]
    actualiser_points_maison(maisons, nom_maison_joueur, score_quiz)
    print("--- Classement Actuel des Maisons ---\n")
    afficher_maison_gagnante(maisons)
    print("--- Profil du Joueur après Chapitre 3 ---\n")
    afficher_personnage(personnage)
    print("<<< Fin du Chapitre 3 ! Préparez-vous pour le grand événement de fin d'année... >>>\n")





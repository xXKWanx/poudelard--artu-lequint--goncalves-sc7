from utils.input_utils import demander_choix
from chapitres.chapitre_1 import lancer_chapitre_1
from chapitres.chapitre_2 import lancer_chapitre_2
from chapitres.chapitre_3 import lancer_chapitre_3

def afficher_menu_principal():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Lancer l'aventure (Chapitre 1)")
    print("2. Quitter le jeu")


def lancer_choix_menu():
    maisons = {"Gryffondor": 0, "Serpentard": 0, "Poufsouffle": 0, "Serdaigle": 0}
    continuer = True
    chapitre_actuel = 1

    while continuer:
        afficher_menu_principal()
        options = ["Lancer l'aventure", "Quitter"]
        choix = demander_choix("Que voulez-vous faire ?", options)

        if choix == "Lancer l'aventure":
            if chapitre_actuel == 1:
                joueur = lancer_chapitre_1()
                chapitre_actuel = 2

            if chapitre_actuel == 2:
                lancer_chapitre_2(joueur)
                chapitre_actuel = 3

            if chapitre_actuel == 3:
                lancer_chapitre_3(joueur, maisons)
                chapitre_actuel = 4



        elif choix == "Quitter":
            print("Au revoir, à bientôt à Poudlard !")
            continuer = False
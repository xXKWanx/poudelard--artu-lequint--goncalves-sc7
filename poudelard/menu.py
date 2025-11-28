import sys
from utils.input_utils import demander_choix
from chapitres.chapitre_1 import lancer_chapitre_1

def afficher_menu_principal():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Lancer l'aventure (Chapitre 1)")
    print("2. Quitter le jeu")

def lancer_choix_menu():
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }

    while True:
        afficher_menu_principal()
        options = ["Lancer l'aventure", "Quitter"]
        choix = demander_choix("Que voulez-vous faire ?", options)

        if choix == "Lancer l'aventure":
            joueur = lancer_chapitre_1()
        elif choix == "Quitter":
            print("Au revoir, à bientôt à Poudlard !")
            sys.exit()
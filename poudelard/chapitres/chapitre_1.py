import sys
from poudelard.univers.personnage import afficher_personnage, initialiser_personnage, modifier_argent, ajouter_objet
from poudelard.utils.input_utils import demander_texte, demander_nombre, demander_choix, load_fichier


def introduction():
    print("===PROJET POUDLARD===\n")
    print("Bonjour et bienvenue dans le jeu (officiel bien sûr) de Harry Potter !\n")
    print("Etes-vous prêt à partir à l'aventure dans ce monde fantastique ?\n")
    print("Si tel est le cas, alors bon courage et aumsez-vous bien!\n")

def creer_personnage():
    nom = demander_texte("Entrez le nom de votre personnage : ")

    prenom = demander_texte("Entrez le prénom de votre personnage : ")

    print("Choisissez vos qualités :\n")

    courage = demander_nombre("Niveau de courage (1-10) : ", 1, 10)

    intelligence = demander_nombre("Niveau de intelligence (1-10) : ",1 , 10)

    loyaute = demander_nombre("Niveau de loyauté (1-10) : ", 1, 10)

    ambition = demander_nombre("Niveau de ambition (1-10) : ", 1, 10)

    attributs = {"courage" : courage, "intelligence" : intelligence, "loyaute" : loyaute, "ambition" : ambition}

    joueur = initialiser_personnage(nom, prenom, attributs)

    afficher_personnage(joueur)

    return joueur


def recevoir_lettre():
    print("Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard...\n")
    print("« Cher élève,\nNous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard ! »\n")
    choix = demander_choix("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?", ["Oui, bien sûr !", "Non, je préfère rester avec l’oncle Vernon..."])
    if choix == 2:
        print("Vous déchirez la lettre, l’oncle Vernon pousse un cri de joie:\n« EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! »\nLe monde magique ne saura jamais que vous existiez... Fin du jeu.\n")
        sys.exit(0)
    else:
        print("Fantastique ! L'aventure commence. Vous vous préparez pour votre fabuleuse aventure.\n")


def rencontrer_hagrid(personnage):
    print(f"Hagrid: Comment y va {personnage['Prenom']} ! Aujourd'hui on va faire du shopping {personnage['Prenom']}, et t'aider à faire tes achats sur le Chemin de Traverse")
    choix = demander_choix("Voulez-vous suivre Hagrid ?", ["Oui", "Non"])

    if choix == "Non":
        print("Hagrid va quand même insister gentiment et vous entraîne quand même avec lui !")

def acheter_fournitures(personnage):

    print("Bienvenue sur le Chemin de Traverse !")
    catalogue = load_fichier("data/inventaire.json")

    objets_obligatoires = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]
    achats_faits = []

    print("Catalogue des objets disponibles :")
    for cle, article in catalogue.items():
        print(f"{cle}. {article[0]} - {article[1]} galions")

    while len(achats_faits) < 3:
        print(f"Vous avez {personnage['Argent']} galions.")
        restant = [obj for obj in objets_obligatoires if obj not in achats_faits]
        print(f"Objets obligatoires restant à acheter : {', '.join(restant)}")

        choix = str(demander_nombre("Entrez le numéro de l'objet à acheter : ", 1, 8))

        if choix in catalogue:
            nom_objet, prix = catalogue[choix]

            if nom_objet in achats_faits:
                print("Vous ne pouvez pas vous avez déjà acheté cet objet.")
            elif nom_objet not in objets_obligatoires:
                print("Concentrez-vous d'abord sur les objets obligatoires !")
            elif personnage['Argent'] < prix:
                print("Vous n'avez plus assez d'argent ! Fin de la partie.")
                sys.exit()
            else:
                modifier_argent(personnage, -prix)
                ajouter_objet(personnage, "Inventaire", nom_objet)
                achats_faits.append(nom_objet)
                print(f"Vous avez acheté {nom_objet} (-{prix} galions).")

    print("Tous les objets obligatoires ont été achetés !")
    print("Il est temps de choisir votre animal de compagnie pour Poudlard !")
    print(f"Vous avez {personnage['Argent']} galions.")

    animaux = ["Chouette", "Chat", "Rat", "Crapaud"]
    prix_animaux = [20, 15, 10, 5]

    print("Voici les animaux disponibles :")
    for i in range(len(animaux)):
        print(f"{i + 1}. {animaux[i]} - {prix_animaux[i]} galions")

    choix_animal = demander_nombre("Quel animal voulez-vous ? ", 1, 4)
    animal_choisi = animaux[choix_animal - 1]
    prix_animal = prix_animaux[choix_animal - 1]

    if personnage['Argent'] >= prix_animal:
        modifier_argent(personnage, -prix_animal)
        ajouter_objet(personnage, "Inventaire", animal_choisi)
        print(f"Vous avez choisi {animal_choisi} (-{prix_animal} galions).")
    else:
        print("Vous n'avez pas assez d'argent. Vous partez sans animal.")
        sys.exit()

    print("Tous les objets obligatoires ont été achetés avec succès ! Voici votre inventaire final :")
    afficher_personnage(personnage)

def lancer_chapitre_1():
    print("==================================================")
    print("                 CHAPITRE 1: L'ARRIVÉE             ")
    print("==================================================")
    introduction()
    joueur = creer_personnage()
    recevoir_lettre()
    rencontrer_hagrid(joueur)
    acheter_fournitures(joueur)
    print("\n<<< Fin du Chapitre 1 ! Votre aventure commence à Poudlard... >>>")
    return joueur
from random import randint, choice
from poudelard.utils.input_utils import load_fichier
from poudelard.univers.maison import actualiser_points_maison
from poudelard.univers.personnage import afficher_personnage
from poudelard.univers.maison import afficher_maison_gagnante

def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):
    equipe = {
        'nom': maison,
        'score': 0,
        'a_marque': 0,
        'a_stoppe': 0,
        'attrape_vifdor': False,
        'joueurs': equipe_data[maison]['joueurs']
    }

    if est_joueur and joueur is not None:
        liste = []
        nom_joueur = f"{joueur['Prenom']} {joueur['Nom']} (Attrapeur)"
        liste.append(nom_joueur)

        for membre in equipe['joueurs']:
            if "(Attrapeur)" not in membre:
                liste.append(membre)

        equipe['joueurs'] = liste

    return equipe


import random


def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba_but = random.randint(1, 10)

    if proba_but >= 6:
        if joueur_est_joueur:
            buteur = equipe_attaque['joueurs'][0]
        else:
            buteur = random.choice(equipe_attaque['joueurs'])

        equipe_attaque['score'] += 10
        equipe_attaque['a_marque'] += 1
        print(f"« {buteur} marque un but pour {equipe_attaque['nom']}! (+10 points) »")
    else:
        equipe_defense['a_stoppe'] += 1
        print(f"« {equipe_defense['nom']} bloque l'attaque ! »")

def apparition_vifdor():
    apparition = random.randint(1,6)
    if apparition == 6:
        return True
    else:
        return False

def attraper_vifdor(e1, e2):
    equipe_gagnante = random.choice([e1, e2])
    equipe_gagnante['score'] += 150
    equipe_gagnante['attrape_vifdor'] = True
    return equipe_gagnante

def afficher_score (e1, e2):
    print ("Score actuel :")
    print(f"{e1['nom']} : {e1['score']} points")
    print(f"{e2['nom']} : {e2['score']} points")

def afficher_equipe(maison, equipe):
    print(f"Équipe de {maison} :")
    for joueur in equipe["joueurs"]:
        print(joueur)


def match_quidditch(joueur, maisons):
    data_equipes = load_fichier("data/equipes_quidditch.json")
    maison_joueur = joueur["Maison"].strip()

    nom_restants = []
    for m in data_equipes.keys():
        if m != maison_joueur:
            nom_restants.append(m)

    maison_adverse = random.choice(nom_restants)
    equipe_joueur = creer_equipe(maison_joueur, data_equipes, True, joueur)
    equipe_adverse = creer_equipe(maison_adverse, data_equipes)

    print(f"Match de Quidditch : {maison_joueur} vs {maison_adverse} !\n")
    afficher_equipe(maison_joueur, equipe_joueur)
    afficher_equipe(maison_adverse, equipe_adverse)
    print(f"Tu joues pour {maison_joueur} en tant qu'Attrapeur\n")

    tour = 1
    vif_attrape = False
    while tour <= 20 and not vif_attrape:
        print(f"Tour {tour}\n")
        tentative_marque(equipe_joueur, equipe_adverse, True)
        tentative_marque(equipe_adverse, equipe_joueur, False)
        afficher_score(equipe_joueur, equipe_adverse)

        if apparition_vifdor():
            equipe_vif = attraper_vifdor(equipe_joueur, equipe_adverse)
            print(f"Le Vif d'Or a été attrapé par {equipe_vif['nom']} ! (+150 points)")
            vif_attrape = True
        else:
            input("Appuyez sur Entrée pour continuer")
            tour += 1

    print("Fin du match !\n")
    afficher_score(equipe_joueur, equipe_adverse)

    if equipe_joueur['score'] > equipe_adverse['score']:
        print(f"La maison gagnante est {maison_joueur} !\n")
        actualiser_points_maison(maisons, maison_joueur, 500)
    elif equipe_adverse['score'] > equipe_joueur['score']:
        print(f"La maison gagnante est {maison_adverse} !\n")
        actualiser_points_maison(maisons, maison_adverse, 500)
    else:
        print("Match nul !")


def lancer_chapitre4_quidditch(joueur, maisons):
    print("==================================================\n")
    print("         CHAPTER 4: LE MATCH DE QUIDDITCH         \n")
    print("==================================================\n")
    match_quidditch(joueur, maisons)
    print("Fin du Chapitre 4 ! Quelle performance incroyable sur le terrain !\n")
    print("Annonce du vainqueur de la Coupe des Quatre Maisons :\n")
    afficher_maison_gagnante(maisons)
    print("Résumé final de votre personnage :\n")
    afficher_personnage(joueur)
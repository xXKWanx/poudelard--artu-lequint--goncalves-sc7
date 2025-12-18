from random import randint, choice

def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):
    equipe = {
        'nom': maison,
        'score': 0,
        'a_marque': 0,
        'a_stoppe': 0,
        'attrape_vifdor': False,
        'joueurs': equipe_data[maison]
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

def afficher_score (e1, e2):
    print ("Score actuel :")
    print(f"{e1['nom']} : {e1['score']} points")
    print(f"{e2['nom']} : {e2['score']} points")

def afficher_equipe(maison, equipe):
    print (f"Equipe de : {maison}")


def initialiser_personnage(nom, prenom, attributs):
    personnage = {"Nom" : nom,
                  "Prenom" : prenom,
                  "Argent" : 100,
                  "Inventaire" : [],
                  "Sortilèges" : [],
                  "Attributs" : attributs}

    return personnage


def afficher_personnage(joueur):
    print("Profil du personnage:")
    print(f"Nom : {joueur['Nom']}")
    print(f"Prenom : {joueur['Prenom']}")
    print(f"Argent: {joueur['Argent']}")
    inventaire_str = ", ".join(joueur['Inventaire'])
    sortileges_str = ", ".join(joueur['Sortilèges'])
    print(f"Inventaire : {inventaire_str}")
    print(f"Sortilèges : {sortileges_str}")
    print("Attributs :")
    for cle, valeur in joueur['Attributs'].items():
        print(f"{cle}: {valeur}")

def modifier_argent(joueur, montant):
    joueur["Argent"] += montant

def ajouter_objet(joueur, cle, objet):
    joueur[cle].append(objet)
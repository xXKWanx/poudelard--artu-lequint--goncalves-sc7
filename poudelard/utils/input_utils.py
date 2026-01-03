import json

def demander_texte(message):
    texte = input(message).strip()
    return texte


def demander_nombre(message, min_val=None, max_val=None):
    while True:
        saisie = input(message).strip()
        if saisie == "":
            continue

        est_valide = True
        debut = 0

        if saisie[0] == "-":
            debut = 1
            if saisie == "-":
                est_valide = False

        partie_chiffres = saisie[debut:]
        if partie_chiffres == "":
            est_valide = False

        for caractere in partie_chiffres:
            if caractere < "0" or caractere > "9":
                est_valide = False

        if est_valide:
            valeur = int(saisie)
            if (min_val is None or valeur >= min_val) and (max_val is None or valeur <= max_val):
                return valeur
            else:
                print(f"Erreur : entrez un nombre entre {min_val} et {max_val}.")
        else:
            print("Erreur : veuillez entrer un nombre entier.")


def demander_choix(message, options):
    print(f"\n{message}")

    index = 1
    for opt in options:
        print(f"{index}. {opt}")
        index += 1

    nb_options = 0
    for opt in options:
        nb_options += 1

    choix_num = demander_nombre("Votre choix : ", 1, nb_options)

    actuel = 1
    for opt in options:
        if actuel == choix_num:
            return opt
        actuel += 1


def load_fichier(chemin_fichier):
    with open(chemin_fichier, 'r',  encoding = 'utf-8') as f:
        return json.load(f)
import json

def demander_texte(message):
    while True:
        texte = input(message).strip()
        if texte:
            return texte


def demander_nombre(message, min_val=None, max_val=None):
    while True:
        saisie = input(message).strip()

        if saisie.startswith("-"):
            chaine_verif = saisie[1:]
        else:
            chaine_verif = saisie

        if chaine_verif.isdigit() and chaine_verif:
            valeur = int(saisie)
            if (min_val is None or valeur >= min_val) and (max_val is None or valeur <= max_val):
                return valeur

        print("Veuillez entrer un nombre entier valide.")


def demander_choix(message, options):
    print(message)
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")

    choix_index = demander_nombre("Votre choix : ", 1, len(options))
    return options[choix_index - 1]


def load_fichier(chemin_fichier):
    with open(chemin_fichier, 'r') as f:
        return json.load(f)
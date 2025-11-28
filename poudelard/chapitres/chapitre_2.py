from poudelard.utils.input_utils import demander_choix


def rencontrer_amis(joueur):
    print("Vous montez à bord du Poudlard Express. Le train se lance, accélère et part en direction du Nord...")
    print("Un jeune homme entre dans votre compartiment, il est beau et fort")

    print("Salut! Moi c'est Ron Weasley. Tu veux bien qu'on s'assoie ensemble ?")
    choix_ron = demander_choix("Que répondez-vous ?", ["Bien sûr, assieds-toi !", "Désolé, je préfère voyager seul."])

    if choix_ron == "Bien sûr, assieds-toi !":
        joueur['Attributs']['loyauté'] += 1
        print("Ron sourit : Génial ! Tu verras, Poudlard, c'est incroyable !")
    else:
        joueur['Attributs']['ambition'] += 1
        print("Ron hausse les épaules et part chercher une autre place.")

    print("Une fille entre ensuite, portant déjà une pile de livres.")
    print("Bonjour, je m'appelle Hermione Granger. Vous avez déjà lu 'Histoire de la Magie'?")

    choix_hermione = demander_choix("Que répondez-vous ?", ["Oui, j'adore apprendre de nouvelles choses !",
                                                            "Euh... non, je préfère les aventures aux bouquins."])

    if choix_hermione == "Oui, j'adore apprendre de nouvelles choses !":
        joueur['Attributs']['intelligence'] += 1
        print("Hermione sourit : C'est fascinant, n'est-ce pas ?")
    else:
        joueur['Attributs']['courage'] += 1
        print("Hermione fronce les sourcils : Il faudrait pourtant s'y mettre un jour !")

    print("Puis un garçon blond entre avec un air arrogant.")
    print("Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?")

    choix_drago = demander_choix("Comment réagissez-vous ?",
                                 ["Je lui serre la main poliment.", "Je l'ignore complètement.",
                                  "Je lui réponds avec arrogance."])

    if choix_drago == "Je lui serre la main poliment.":
        joueur['Attributs']['ambition'] += 1
        print("Drago hoche la tête avec satisfaction.")
    elif choix_drago == "Je l'ignore complètement.":
        joueur['Attributs']['loyauté'] += 1
        print("Drago fronce les sourcils, vexé : Tu le regretteras !")
    else:
        joueur['Attributs']['courage'] += 1
        print("Drago vous lance un regard noir avant de partir.")

    print("Le train continue sa route. Le château de Poudlard se profile à l'horizon...")
    print("Tes choix semblent déjà en dire long sur ta personnalité !")
    print(f"Tes attributs mis à jour : {joueur['Attributs']}")
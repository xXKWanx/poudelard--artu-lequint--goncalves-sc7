

# Projet Poudlard – L’Art de Coder comme un Sorcier

Projet réalisé dans le cadre du module **TI101 – Programmation en Python**.
Il s’agit d’un **jeu d’aventure interactif en Python**, inspiré de l’univers de *Harry Potter*, dans lequel le joueur incarne un élève découvrant le monde magique et Poudlard à travers plusieurs chapitres.



## Auteurs

* **GONCALVES Matias** – *GitHub :* `6ScriptSavvy9`
* **Kérywan ARTU--LEQUINT** – *GitHub :* `xXKWanx`

Projet réalisé **en binôme**.



## Description du projet

Le jeu est découpé en **4 chapitres**, correspondant aux grandes étapes de l’arrivée du joueur à Poudlard :

* Création du personnage et découverte du monde magique
* Voyage vers Poudlard et cérémonie de répartition
* Apprentissage des sorts et quiz de magie
* Match de Quidditch (chapitre final)

Le projet exploite :

* Les **fonctions** et la **modularisation**
* Les **dictionnaires**, **listes** et **fichiers JSON**
* La **gestion des choix utilisateur**
* Des **événements interactifs et aléatoires**



## Structure du projet

```
poudelard/
│
├── main.py
├── menu.py
│
├── chapitres/
│   ├── chapitre_1.py
│   ├── chapitre_2.py
│   ├── chapitre_3.py
│   └── chapitre_4.py
│
├── univers/
│   ├── personnage.py
│   └── maison.py
│
├── utils/
│   └── input_utils.py
│
└── data/
    ├── maisons.json
    ├── sorts.json
    ├── quiz_magie.json
    ├── inventaire.json
    └── equipes_quidditch.json
```



## Répartition des tâches

### Chapitre 1 – Arrivée dans le monde magique

**Kérywan**

* `introduction()`
* `creer_personnage()`
* `recevoir_lettre()`

**Matias**

* `rencontrer_hagrid()`
* `acheter_fournitures()`
* `lancer_chapitre_1()`



### Utils (`utils/input_utils.py`)

 **Entièrement réalisé par Matias**



### Gestion du personnage (`univers/personnage.py`)

**Kérywan**

* `initialiser_personnage()`
* `afficher_personnage()`

**Matias**

* `modifier_argent()`
* `ajouter_objet()`



### Chapitre 2 – Voyage et répartition

**Matias**

* `rencontrer_amis()`
* `mot_de_bienvenue()`
* `ceremonie_repartition()`

**Kérywan**

* `installation_salle_commune()`
* `lancer_chapitre_2()`

**Maisons (entièrement Kérywan)**

* `actualiser_points_maison()`
* `afficher_maison_gagnante()`
* `repartition_maison()`



### Chapitre 3 – Sorts et quiz magique

**Kérywan**

* `apprendre_sorts()`

**Matias**

* `quiz_magie()`
* `lancer_chapitre_3()`



### Chapitre 4 – Match de Quidditch

**Kérywan**

* `creer_equipe()`
* `tentative_marque()`
* `apparition_vifdor()`
* `attraper_vifdor()`

**Matias**

* `afficher_score()`
* `afficher_equipe()`
* `match_quidditch()`
* `lancer_chapitre4_quidditch()`



## Organisation du travail

* Le projet a été développé **de manière progressive**
* **Un chapitre par semaine** a été réalisé
* Des tests réguliers ont permis de garantir la stabilité du jeu



## État du projet

**Tout est fonctionnel**
* Toutes les fonctionnalités demandées sont implémentées
* Le projet respecte l’architecture et les contraintes imposées



##  Lancer le jeu

Assurez-vous d’être à la racine du projet, puis exécutez :

```bash
python main.py
```



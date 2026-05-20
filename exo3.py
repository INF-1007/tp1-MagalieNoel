# -*- coding: utf-8 -*-
# Exercice 03 - Choisir le meilleur trajet vers le Parc Jean-Drapeau (gabarit)
"""
Objectif :
- DEMANDER : distance (km, float), attente_velo (min, float), temps_metro (min, float), controle (min, float)
- Valider : toutes les valeurs >= 0
- Calculer les temps bruts (minutes) :
    marche = distance * 60 / 5 + controle
    velo   = attente_velo + distance * 60 / 15 + controle
    metro  = temps_metro + controle
- Arrondir chaque temps a la minute superieure (ceil)
- Determiner la/les option(s) minimale(s)

Sortie :
- 1 option gagnante : "Option la plus rapide : marcher." ou "velo." ou "metro."
- 2 options ex-aequo (ordre : marcher, velo, metro) : "Egalite : X et Y."
- 3 options ex-aequo : "Egalite : marcher, velo et metro."

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS :
1) "Entrez la distance jusqu'au Parc Jean-Drapeau (en kilometres) : "
2) "Entrez le temps d'attente pour un velo en libre-service (en minutes) : "
3) "Entrez le temps du trajet en metro (en minutes) : "
4) "Entrez le temps de controle a l'entree (en minutes) : "
"""

# TODO: Importer math
import math
vitesseMarche = 5 #km/h
vitesseVelo = 15 #km/h
uneHeure = 60 #minutes

# TODO: Lire les 4 valeurs
try:
    distance = float(input("Entrez la distance jusqu'au Parc Jean-Drapeau (en kilometres) : "))
    attenteVelo = float(input("Entrez le temps d'attente pour un velo en libre-service (en minutes) : "))
    trajetMetro = float(input("Entrez le temps du trajet en metro (en minutes) : "))
    controle = float(input("Entrez le temps de controle a l'entree (en minutes) : "))
# TODO: Validation
    if distance < 0 or attenteVelo < 0 or trajetMetro < 0 or controle < 0:
        raise ValueError
    
    # TODO: Calculer, arrondir (ceil) et determiner le(s) meilleur(s)
    else: 
        marche = math.ceil(distance * uneHeure / vitesseMarche + controle)

        velo = math.ceil(attenteVelo + (distance * uneHeure) / vitesseVelo + controle)

        metro = math.ceil(trajetMetro + controle)

        minimum = min(marche, velo, metro)

        options = []
        if minimum == marche:
            options.append("marcher")
        if minimum == velo:
            options.append("velo")
        if minimum == metro:
            options.append("metro")

        # TODO: Afficher la phrase exacte
        if len(options) == 1:
            print(f"Option la plus rapide : {options[0]}.")
        if len(options) == 2:
            print(f"Egalite : {options[0]} et {options[1]}.")
        if len(options) == 3:
            print(f"Egalite : {options[0]}, {options[1]} et {options[2]}.")

except ValueError:
    print("Erreur - donnees invalides.")


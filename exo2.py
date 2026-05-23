# Exercice 02 - Affluence sur les scenes (P a W) (gabarit)
"""
Objectif :
- Lire 8 entiers (un par ligne) : personnes devant les scenes P, Q, R, S, T, U, V, W (dans cet ordre)
- Valider : chaque valeur est un entier >= 0
    -> sinon afficher EXACTEMENT : "Erreur - donnees invalides."
- Calculer l'intensite brute par scene : intensite = personnes * facteur
- Normaliser sur 0..10 avec un arrondi half-up :
    - maxI = max(intensites)
    - si maxI == 0 : niveaux = [0]*8
    - sinon : niveau = int((intensite / maxI) * 10 + 0.5), borne dans [0,10]
- Afficher une grille verticale :
    - lignes 10 a 1
    - colonnes P a W
    - afficher "❚" si niveau_scene >= niveau_ligne sinon "."
    - un espace entre chaque cellule
    - format de ligne : "{ligne:2} | <8 cellules>"
    - derniere ligne : "     P Q R S T U V W"
"""

FACTEURS = [1.20, 1.15, 1.05, 0.90, 0.90, 1.05, 1.15, 1.20]

# TODO: Lire 8 entiers (un par ligne) dans une liste personnes
#       En cas d'erreur de conversion ou valeur negative -> afficher le message d'erreur et quitter
valeurs = []
try:
    for valeur in range(8):
        valeur = int(input())
        if valeur < 0:
            raise ValueError
        else:
            valeurs.append(valeur)
    intensiteBrutes = []
# TODO: Calculer les intensites brutes (liste de 8 floats)
    for i in range(8):
        intensiteBrutes.append(valeurs[i] * FACTEURS[i])
    # TODO: Calculer les niveaux normalises (liste de 8 entiers dans [0,10])
    maxl = intensiteBrutes[0]
    for intensiteBrute in intensiteBrutes:
        if intensiteBrute > maxl:
            maxl = intensiteBrute
    niveaux = []
    if maxl != 0:
        for i in range(8):
            niveaux.append(max(0, min((int((intensiteBrutes[i] / maxl) * 10 + 0.5), 10))))
    # TODO: Afficher la grille (10 lignes) puis la ligne des labels
    else:
        for i in range(8):
            niveaux.append(0)
    output = ""
    for i in range(10, 0, -1):
        output += f"{(i):2d} |"

        for j in range(8):
            if(niveaux[j] >= i):
                output += " ❚"
            else:
                output += " ."
        output += "\n"
    
    output += "     P Q R S T U V W"
    print(f"{output}")
except ValueError:
    print("Erreur - donnees invalides.")


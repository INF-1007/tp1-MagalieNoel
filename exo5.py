# -*- coding: utf-8 -*-
# Exercice 05 - Planification d'achat de billets de festival (gabarit)
"""
Objectif :
- DEMANDER : n (int) et statut benevole (O/N)
- Options :
    20 journees : 80.00$
    10 journees : 44.00$
     4 journees : 18.00$
     1 journee  :  5.00$
- Reduction : si benevole = O, appliquer 10% de reduction sur le cout des forfaits uniquement.
  Les billets journaliers ne sont pas reduits.

But :
- Acheter au moins n billets
- Minimiser le prix total
- En cas d'egalite sur le prix : choisir le plus petit total de billets, puis le plus petit nombre de billets journaliers

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Sinon, afficher EXACTEMENT 6 lignes :
    Forfaits de 20 journees - A
    Forfaits de 10 journees - B
    Forfaits de 4 journees - C
    Billets journaliers - D
    Total billets - T
    Prix total - PPP.PP$

Prompts EXACTS :
1) "Entrez le nombre de billets necessaires : "
2) "Entrez le statut benevole (O/N) : "

Conseil :
- Une solution simple consiste a tester plusieurs combinaisons de forfaits avec des boucles (bruteforce).
"""

# TODO: Lire n (int) et statut (str)
try:
    n = int(input("Entrez le nombre de billets necessaires : "))
    statut = input("Entrez le statut benevole (O/N) : ")
    # TODO: Validation (n >= 0 et statut dans {O, N})
    if n < 0:
        raise ValueError
    possibilites = ["O", "N"]
    if possibilites[0] != statut and possibilites[1] != statut:
        raise ValueError
    # TODO: Chercher la meilleure combinaison (A, B, C, D)
    essais = []
    for i in range((n // 20) + 1):
        for j in range((n //  10) + 1):
            for k in range((n // 4) + 1):
                for l in range (n + 1):
                    nbBillets = 20 * i + 10 * j + 4 * k + l
                    if nbBillets >= n:
                        essaiPrix = i * 80 + j * 44 + k * 18 + l * 5
                        if statut == possibilites[0]:
                            essaiPrix = 0.9*(i * 80 + j * 44 + k * 18) + l * 5
                        essaiInfos = [essaiPrix, i, j, k, l, nbBillets]
                        essais.append(essaiInfos)

    meilleur = essais[0]
    for essai in essais:
        if essai[0] < meilleur[0]:
                meilleur = essai
        elif essai[0] == meilleur[0]:
            if essai[-1] < meilleur[-1]:
                meilleur = essai
            elif essai[-1] ==  meilleur[-1]:
                if essai[-2] < meilleur[-2]:
                    meilleur = essai

# TODO: Calculer et afficher le resultat exact (6 lignes)
    print(f"Forfaits de 20 journees - {meilleur[1]}")
    print(f"Forfaits de 10 journees - {meilleur[2]}")
    print(f"Forfaits de 4 journees - {meilleur[3]}")
    print(f"Billets journaliers - {meilleur[4]}")
    print(f"Total billets - {meilleur[-1]}")
    print(f"Prix total - {meilleur[0]:02.2f}$")

except ValueError:
    print("Erreur - donnees invalides.")


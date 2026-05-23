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
    t=n
    a = n // 20
    n %= 20
    
    b = n // 10
    n %= 10

    c = n // 4
    n %= 4

    d= n

# TODO: Calculer et afficher le resultat exact (6 lignes)
    
    prix = a * 80 + b * 44 + c * 18 + d * 5
    if statut == possibilites[0]:
        prix = 0.9*(a * 80 + b * 44 + c * 18) + d * 5
    print(f"Forfaits de 20 journees - {a}")
    print(f"Forfaits de 10 journees - {b}")
    print(f"Forfaits de 4 journees - {c}")
    print(f"Billets journaliers - {d}")
    print(f"Total billets - {t}")
    print(f"Prix total - {prix:02.2f}$")

except ValueError:
    print("Erreur - donnees invalides.")


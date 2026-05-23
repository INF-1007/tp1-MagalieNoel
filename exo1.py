# -*- coding: utf-8 -*-
# Exercice 01 - Bilan d'ecoute au festival (gabarit)
"""
Objectif :
- DEMANDER : nom complet, spectacles electroniques, duree electronique, spectacles live, duree live
- Valider : spectacles >= 0 et durees > 0 (entiers)
- Convertir les minutes en format HhMM (minutes sur 2 chiffres)
- Afficher EXACTEMENT 4 lignes :
    Bonjour {nom}
    Electronique: {A} spectacle(s), {He}h{Me:02d} d'ecoute
    Live: {B} spectacle(s), {Hl}h{Ml:02d} d'ecoute
    Total: {Ht}h{Mt:02d}

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS a utiliser :
1) "Entrez votre nom complet : "
2) "Entrez le nombre de spectacles electroniques assistes au festival : "
3) "Entrez la duree moyenne d'un spectacle electronique (en minutes) : "
4) "Entrez le nombre de spectacles live assistes au festival : "
5) "Entrez la duree moyenne d'un spectacle live (en minutes) : "
"""

# TODO: Lire le nom (str)
nom = input("Entrez votre nom complet : ")

# TODO: Lire les 4 valeurs (int)
try:
    nbElectronique = int(input("Entrez le nombre de spectacles electroniques assistes au festival : "))
    dureeElec = int(input("Entrez la duree moyenne d'un spectacle electronique (en minutes) : "))
    nbLive = int(input("Entrez le nombre de spectacles live assistes au festival : "))
    dureeLive = int(input("Entrez la duree moyenne d'un spectacle live (en minutes) : "))
except ValueError:
    print("Erreur - donnees invalides.")
# TODO: Valider les donnees (spectacles >= 0, durees > 0)
if nbElectronique < 0 or nbLive < 0:
    print("Erreur - donnees invalides.")
elif dureeElec <= 0 or dureeLive <= 0:
    print("Erreur - donnees invalides.")

# TODO: Calculer les minutes totales (electronique, live, total)
else:
    #electronique
    totalElecMin = nbElectronique * dureeElec 
    #live
    totalLiveMin = nbLive * dureeLive    
    #total
    grandTotal = totalElecMin + totalLiveMin  

    # TODO: Convertir en heures/minutes et afficher exactement 4 lignes
    #electronique
    heuresElec = totalElecMin // 60
    minutesElec = totalElecMin % 60
    #Live
    heuresLive = totalLiveMin // 60
    minutesLive = totalLiveMin % 60
    #total
    heuresTotal = grandTotal // 60
    minutesTotal = grandTotal % 60

    print(f"Bonjour {nom}\nElectronique: {nbElectronique} spectacle(s), {heuresElec}h{minutesElec:02d} d'ecoute\nLive: {nbLive} spectacle(s), {heuresLive}h{minutesLive:02d} d'ecoute\nTotal: {heuresTotal}h{minutesTotal:02d}")

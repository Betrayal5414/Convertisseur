from termcolor import *
from liste import *
from calcules import *
from conversion import *

continuer = True

while continuer:
    cprint("Choisissez un numéro dans la liste correspondant aux type de conversion.", "black", "on_yellow")
    for i in liste:
        cprint(f"{i}", "yellow")
    while True:
        try:
            convertisseur = int(input())
        except ValueError:
            cprint("Choisisez un numéro dans la liste","red")
            continue
        if convertisseur >= 1 and convertisseur <= 4:
            break
        else:
            cprint("Le numéro doit être dans la liste", "red")
            
    
    """Convertisseur de Données"""
    if convertisseur == 1:
        donnees(donnees)      
    elif convertisseur == 2:
        temperatures(temperatures)   
    elif convertisseur == 3:
        longueur(longueur)
    elif convertisseur == 4:
        vitesse(vitesse)


    while True:
        cprint("Voulez vous continuer ? oui/non", "white", "on_blue")
        choix = input()
        if choix in ("n", "non", "N", "no"):
            continuer = False
            break
        elif choix in ("o", "oui", "O", "yes"):
            continuer = True
            break
        elif choix not in ("o", "oui", "O", "yes"):
            cprint("je n'ai pas compris", "white", "on_blue")


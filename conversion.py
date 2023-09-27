from termcolor import *
from calcules import *
from liste import *


def donnees(don):
    cprint("Choisissez les données à convertir", "black", "on_yellow")
    for j in liste_donnees:
        cprint(f"{j}", "yellow")
    while True:
        try:
            don = int(input())
        except ValueError:
            cprint("Choisisez un numéro dans la liste","red")
            continue
        if don >= 1 and don <= 4:
            break
        else:
            cprint("Le numéro doit être dans la liste", "red")
    if don == 1:
        Mo = float(input("Megaoctet : "))
        megaoctet(Mo)
    elif don == 2:
        Mb = float(input("Megabits : "))
        megabits(Mb)
    elif don == 3:
        Go = float(input("Gigaoctet : "))
        gigaoctet(Go)
    elif don == 4:
        Gb = float(input("Gigabits : "))
        gigabits(Gb)
        
def temperatures(temp):
    cprint("Choisisser les températures à convertir", "black", "on_yellow")
    for j in liste_temperature:
        cprint(f"{j}", "yellow")
    while True:
        try:
            temp = float(input())
        except ValueError:
            cprint("Choisisez un numéro dans la liste","red")
            continue
        if temp >= 1 and temp <= 2:
            break
        else:
            cprint("Le numéro doit être dans la liste", "red")
    if temp == 1:
        C = float(input("Celsuis : "))
        celsuis(C)
    elif temp == 2:
        F = float(input("Fahrenheit : "))
        fahrenheit(F)
        
def longueur(long):
    cprint("Choissir les longueurs à convertir dans la liste de données", "black", "on_yellow")
    for j in liste_longueurs:
        cprint(f"{j}", "yellow")
    while True:
        try:
            long = float(input())
        except ValueError:
            cprint("Choisisez un numéro dans la liste","red")
            continue
        if long >= 1 and long <= 10:
            break
        else:
            cprint("Le numéro doit être dans la liste", "red")
    if long == 1:
        Cm = float(input("Centimères : "))
        centimetre(Cm)
    elif long == 2:
        P = float(input("Pouces : "))
        pouce(P)
    elif long == 3:
        M = float(input("Mètres : "))
        metrep(M)
    elif long == 4:
        Pi = float(input("Pieds : "))
        pied(Pi)
    elif long == 5:
        M = float(input("Mètres : "))
        metrey(M)
    elif long == 6:
        Y = float(input("Yards : "))
        yards(Y)
    elif long == 7:
        Km = float(input("Kilomètres : "))
        kilometremi(Km)
    elif long == 8:
        Mi = float(input("Miles : "))
        mile(Mi)
    elif long == 9:
        Km = float(input("Kilomètres : "))
        kilomteremm(Km)
    elif long == 10:
        Mm = float(input("Milles Marins : "))
        millemarin(Mm)
        
def vitesse(vit):
    cprint("Choissir les vitessses à convertir dans la liste de données", "black", "on_yellow")
    for j in liste_vitesse:
        cprint(f"{j}", "yellow")
    while True:
        try:
            vit = float(input())
        except ValueError:
            cprint("Choisisez un numéro dans la liste","red")
            continue
        if vit >= 1 and vit <= 6:
            break
        else:
            cprint("Le numéro doit être dans la liste", "red")
    if vit == 1:
        Kmh = float(input("Km/h : "))
        kilometrem(Kmh)
    elif vit == 2:
        Ms = float(input("M/s : "))
        metrek(Ms)
    elif vit == 3:
        Kmh = float(input("Km/h : "))
        kilometremi(Kmh)
    elif vit == 4:
        Mh = float(input("Mile/h : "))
        milesk(Mh)
    elif vit == 5:
        Kmh = float(input("Km/h : "))
        kilometren(Kmh)
    elif vit == 6:
        No = float(input("Noeud : "))
        noeud(No)
        


    
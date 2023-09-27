
from termcolor import *

def megaoctet(Mo):
    Mb = Mo * 8
    Gb = Mb / 1000
    cprint(f"{Mo} Mo = {Mb} Mb / {Gb} Gb", "white", "on_green", attrs=["bold"])
    
def megabits(Mb):
    Mo = Mb / 8
    Go = Mo / 1000
    cprint(f"{Mb} Mb = {Mo} Mo / {Go} Go", "white", "on_green", attrs=["bold"])
    
def gigaoctet(Go):
    Gb = Go * 8
    Mb = Gb * 1000
    cprint(f"{Go} Go = {Gb} Gb / {Mb} Mb", "white", "on_green", attrs=["bold"])
    
def gigabits(Gb):
    Go = Gb / 8
    Mo = Go * 1000
    cprint(f"{Gb} Gb = {Go} Go / {Mo} Mo", "white", "on_green", attrs=["bold"])

def celsuis(C):
    F = (C*9/5) + 32
    cprint(f"{C}°C = {F}°F", "white", "on_green", attrs=["bold"])
    
def fahrenheit(F):
    C = (F-32)*5/9
    cprint(f"{F}°F = {C}°C", "white", "on_green", attrs=["bold"])
    
def centimetre(Cm):
    P = Cm/2.54
    cprint(f"{Cm} Cm = {P} Pouces", "white", "on_green", attrs=["bold"])

def pouce(P):
    Cm = P*2.54
    cprint(f"{P} pouces = {Cm} Cm", "white", "on_green", attrs=["bold"])
    
def metrep(M):
    Pi = M * 3.281
    cprint(f"{M} Mètres = {round(Pi, 3)} Pieds", "white", "on_green", attrs=["bold"])

def pied(Pi):
    M = Pi / 3.281
    cprint(f"{Pi} Pieds = {round(M, 3)} Mètres", "white", "on_green", attrs=["bold"])
    
def metrey(M):
    Y = M * 1.094
    cprint(f"{M} Mètres = {round(Y, 3)} Yards", "white", "on_green", attrs=["bold"])
    
def yards(Y):
    M = Y / 1.094
    cprint(f"{Y} Yards = {round(M, 3)} Mètres", "white", "on_green", attrs=["bold"])
    
def kilometremi(Km):
    Mi = Km / 1.609
    cprint(f"{Km} Kilomètres = {round(Mi, 3)} Miles", "white", "on_green", attrs=["bold"])
    
def mile(Mi):
    Km = Mi * 1.609
    cprint(f"{Mi} Miles = {round(Km, 3)} Kilomètres", "white", "on_green", attrs=["bold"])

def kilomteremm(Km):
    Mm = Km / 1.852
    cprint(f"{Km} Kilomètres = {round(Mm, 3)} Milles Marins", "white", "on_green", attrs=["bold"])

def millemarin(Mm):
    Km = Mm * 1.852
    cprint(f"{Mm} Milles Marins = {round(Km, 3)} Kilomètres", "white", "on_green", attrs=["bold"])

def kilometrem(Kmh):
    Ms = Kmh / 3.6
    cprint(f"{Kmh} Km/h  = {round(Ms, 3)} M/s", "white", "on_green", attrs=["bold"])

def metrek(Ms):
    Kmh = Ms * 3.6
    cprint(f"{Ms} M/s  = {round(Kmh, 1)} Km/h", "white", "on_green", attrs=["bold"])

def kilometremi(Kmh):
    Mh = Kmh / 1.609
    cprint(f"{Kmh} Km/h  = {round(Mh, 2)} Mile/h", "white", "on_green", attrs=["bold"])

def milesk(Mh):
    Kmh = Mh * 1.609
    cprint(f"{Mh} Mile/h  = {round(Kmh, 2)} Km/h", "white", "on_green", attrs=["bold"])
    
def kilometren(Kmh):
    No = Kmh / 1.852
    cprint(f"{Kmh} Km/h  = {round(No, 2)} Noeuds", "white", "on_green", attrs=["bold"])

def noeud(No):
    Kmh = No * 1.852
    cprint(f"{No} Noeud  = {round(Kmh, 3)} Km/h", "white", "on_green", attrs=["bold"])
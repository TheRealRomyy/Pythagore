# Importer math
from math import *

# Demander ce qu'on veut calculer
print("Que voulez vous calculer ? \n \n1: L'hyphothènuse \n2: Un côté")
toCalc = input()

# Creer la fonction hyphothènuse
def hyphothenuse():
    print("Veuillez donnez la longueure du premier côté ( AB )")
    ab = input()

    print("Veuillez donnez la longeure du deuxième côté ( BC )")
    bc = input()

    print("Bien, votre triangle ABC rectangle en B tel que AB = " + ab + " et BC = " + bc + " !")

    # Calculer l'hyphothènuse
    ac2 = float(bc)*float(bc) + float(ab)*float(ab)
    ac2 = sqrt(ac2)

    print("L'hyphothènuse ( AC ) = " + str(ac2)) 

# Creer la fonction angle
def angle():
    print("Veuillez donnez la longueure du premier côté ( AB )")
    ab = input()

    print("Veuillez donnez la longeure du deuxième côté ( l'Hyphothènuse )")
    hypo = input()

    print("Bien, votre triangle ABC rectangle en B tel que AB = " + ab + " et l'hyphothènuse = " + hypo + " !")

    # Calculer l'angle
    bc2 = float(hypo)*float(hypo) - float(ab)*float(ab)
    bc2 = sqrt(bc2)

    print("BC = " + str(bc2)) 

# Vérifier si toCalc n'est ni 2 ni 1
if toCalc != "1" and toCalc != "2":
    print("Erreur: Vous deviez marqué 2 ou 1 !")
    exit()

# Si toCalc est 1 calculer l'hyphothènuse si c'est 2 calculer un angle
if toCalc == "1":
    hyphothenuse()
    
elif toCalc == "2":
    angle()
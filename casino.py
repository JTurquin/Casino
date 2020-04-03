# -*- coding: utf-8 -*
from random import randrange
from math import ceil
import os



nombre_miser = -1
mise = -1
argent = 1000
continuer_partie = True

print("Vous vous installez à la table de roulette avec", argent, "$.")

while continuer_partie:

    nombre_miser = -1
    mise = -1
    while nombre_miser < 0 or nombre_miser > 49:

        nombre_miser = input("Miser sur un nombre entre 0 et 49 : ")

        try:

            nombre_miser = int(nombre_miser)

        except ValueError:
            print("Vous n'avez pas saisi un nombre.")

            if(nombre_miser < 0):
                print("Le nombre est négatif")
            if(nombre_miser > 49):
                print("le nombre est supérieur à 49")


    while mise < 0 or mise > argent:

        mise = input("Metter une mise : ")

        try:

            mise = int(mise)

        except ValueError:
            print("Vous n'avez pas saisi un nombre.")

            if(mise < 0):
                print("Le nombre est négatif")
            if(mise > argent):
                print("Vous n'avez pas assez d'argent")

    numero_gagnant = randrange(50)
    print("La roulette tourne... ... et s'arrête sur le numéro", numero_gagnant)

    if(numero_gagnant == nombre_miser):
        argent += ceil(3*mise)
    elif(numero_gagnant % 2 == 0):
        argent += ceil(mise/2)
    else:
        argent -= mise

    if argent <= 0:

        print("Vous êtes ruiné ! C'est la fin de la partie.")
        continuer_partie = False

    else:
        print("Vous avez à présent", argent, "$")
        quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")

        if quitter == "o" or quitter == "O":
            print("Vous quittez le casino avec vos gains.")
            continuer_partie = False
        else:
            continuer_partie = True


print("fin")
os.system("pause")

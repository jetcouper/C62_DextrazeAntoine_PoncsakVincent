from sys import argv, exit
from entrainement import Entrainement
from entrainement_to_BD import Entrainement_BD
from recherche import Recherche
from argument import Argument_terminale
from dao import BaseDeDonnees
import numpy as np


def main():
    
    entrainementText = Entrainement()
    argument = Argument_terminale()
    bd = BaseDeDonnees()
    argp =argument.run()
    
    if(argp.b):
        with bd:
            bd.regenerer()


    elif(argp.e):
        with bd:
            print("Mode entrainement activé")
            #À envoyer dans DB
            entrainement_bd = Entrainement_BD()
            matrice, dict = entrainementText.creationMatrice(entrainementText.creationTexte(argp.chemin,argp.encodage),argp.t)
            entrainement_bd.insertion_mots(dict.items())
            liste_tuple = []

            for i, j in np.argwhere(matrice > 0):
                    liste_tuple.append((int(i),int(j),argp.t,int(matrice[i,j])))

            #lexique_bd = entrainement_bd.chargement_lexique()
            entrainement_bd.insertion_coocurrences(liste_tuple)

    elif(argp.p):
        #Entrainement à faire avant la prédiction.
        with bd:
            commande_complete = ""
            print("Mode prédiction activé")
            while commande_complete != "q":
                try:
                    commande_complete = input("Entrez un mot, le nombre de synonymes que vous voulez et la méthode de calcule, i.e. produit scalaire: 0, least-squares:1, city-block: 2\r\nTapez q pour quitter.\r\n")
                    if commande_complete == 'q':
                        break
                    mot, nb_synonymes, methode = commande_complete.split()
                    recherche = Recherche(bd.charger_cooccurrences(argp.t), bd.charger_lexique(), mot, nb_synonymes, methode)
                    print("\r")
                    for key, value in recherche.resultat.items():
                        print(f"{key} --> {value}")
                    print("\r")
                except ValueError:
                    print("Veuillez entrer : mot nombre methode\n")
                    continue

    
if __name__ == '__main__':
    quit(main())
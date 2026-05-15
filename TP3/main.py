from sys import argv, exit
from entrainement import Entrainement
from recherche import Recherche
from argument import Argument_terminale
from dao import BaseDeDonnees
from clustering import Clustering
import numpy as np
import matplotlib.pyplot as plt


def main():
    argument = Argument_terminale()
    argp =argument.run()
    
    
    if(argp.b):
        with BaseDeDonnees() as bd:
            bd.regenerer()

    elif(argp.e):
        with BaseDeDonnees() as bd:
            print("Mode entrainement activé")
            #À envoyer dans DB
            entraineur = Entrainement( argp.t,bd)
            entraineur.entrainer(argp.chemin, argp.encodage)
            
    elif(argp.p):
        #Entrainement à faire avant la prédiction.
        recherche = Recherche()
        with BaseDeDonnees() as bd:
            commande_complete = ""
            print("Mode prédiction activé")
            commande_complete = input("Entrez un mot, le nombre de synonymes que vous voulez et la méthode de calcule, i.e. produit scalaire: 0, least-squares:1, city-block: 2\r\nTapez q pour quitter.\r\n")
            while commande_complete != "q":
                if commande_complete != "":
                    try:
                        mot, nb_synonymes, methode = commande_complete.split()
                        resultat = recherche.recherche(bd.charger_cooccurrences(argp.t), bd.charger_lexique(), mot, nb_synonymes, methode)
                        print("\r")
                        for key, value in resultat.items():
                            print(f"{key} --> {value}")
                        print("\r")
                    except ValueError:
                        print("Veuillez entrer : mot nombre methode\n")
                        continue
                    except Exception as e:
                        print(e)
                    commande_complete = input("Entrez un mot, le nombre de synonymes que vous voulez et la méthode de calcule, i.e. produit scalaire: 0, least-squares:1, city-block: 2\r\nTapez q pour quitter.\r\n")
                else:
                    print("Veuillez entrer une commande valide, un mot, un nombre et une méthode.\n")
                    commande_complete = input("Entrez un mot, le nombre de synonymes que vous voulez et la méthode de calcule, i.e. produit scalaire: 0, least-squares:1, city-block: 2\r\nTapez q pour quitter.\r\n")
    elif(argp.c):
        with BaseDeDonnees() as bd:
            entraineur = Entrainement( argp.t,bd)
            mot_a_index, matrice_coocurance = entraineur.chargerBD(argp.normaliser, argp.conserver)
            commande_complete = ""
            print("Mode cluster activé")
            cluster = Clustering(argp.k,matrice_coocurance,mot_a_index)
            cluster.retourneReponse(argp.n)
            
            if argp.graphe:
                y = cluster.historique_migrations
                x = range(1, len(y) + 1) # Crée une liste [1, 2, 3...] pour l'axe X
                
                plt.plot(x, y, marker='o') # marker='o' met des petits points sur la ligne
                plt.xlabel("Itérations")
                plt.ylabel("Nombre de migrations")
                plt.title("Nombre de migrations en fonction du nombre d’itérations")
                plt.grid(True)
                plt.show()
    
         

    
if __name__ == '__main__':
    quit(main())
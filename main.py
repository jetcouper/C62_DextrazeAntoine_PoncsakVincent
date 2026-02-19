from sys import argv, exit

from entrainement import Entrainement
from recherche import Recherche

def main():
    chemin = argv[1]
    encodage = argv[2]
    #fenetre = argv[3]
    fenetre = 5
    entrainementText = Entrainement(chemin,encodage,fenetre)

    commande_complete = ""
    while commande_complete != "q":
        commande_complete = input("Entrez un mot, le nombre de synonymes que vous voulez et la méthode de calcule, i.e. produit scalaire: 0, least-squares:1, city-block: 2\r\nTapez q pour quitter.\r\n")
        recherche = Recherche(chemin,encodage,entrainementText.matrice,entrainementText.dict,commande_complete)

if __name__ == '__main__':
    quit(main())
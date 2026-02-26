from sys import argv, exit
from entrainement import Entrainement
from recherche import Recherche

def boucle(entrainementText, chemin, encodage):
    commande_complete = ""
    while commande_complete != "q":
        commande_complete = input("Entrez un mot, le nombre de synonymes que vous voulez et la méthode de calcule, i.e. produit scalaire: 0, least-squares:1, city-block: 2\r\nTapez q pour quitter.\r\n")
        if commande_complete == 'q':
            break
        try:
            mot, nb_synonymes, methode = commande_complete.split()
            nb_synonymes = int(nb_synonymes)
            methode = int(methode)
            if methode not in (0, 1, 2):
                print("La méthode doit être 0, 1 ou 2.\n")
                continue
        except ValueError:
            print("Veuillez entrer : mot nombre methode\n")
            continue

        except IndexError:
            print("Veuillez entrer exactement 3 valeurs.\n")
            continue
        recherche = Recherche(chemin,encodage,entrainementText.matrice,entrainementText.dict,mot,nb_synonymes,methode)
        print("\r")
        for key, value in recherche.resultat.items():
            print(f"{key} --> {value}")
        print("\r")

def main():
    chemin = argv[3]
    encodage = argv[2]
    fenetre = argv[1]
    #fenetre = 5
    entrainementText = Entrainement(chemin,encodage,int(fenetre))
    boucle(entrainementText, chemin, encodage)
    
if __name__ == '__main__':
    quit(main())
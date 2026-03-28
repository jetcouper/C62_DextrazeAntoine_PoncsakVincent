import argparse
from entrainement import Entrainement
from recherche import Recherche


class Argument_terminale():
    def run(self):
        parser = argparse.ArgumentParser(description = "Entrez un mot, le nombre de synonymes que vous voulez et la méthode de calcule, i.e. produit scalaire: 0, least-squares:1, city-block: 2\r\nTapez q pour quitter.\r\n")
        
        parser.add_argument("-e", action="store_true", help="Mode entrainement")
        parser.add_argument("-p", action="store_true", help="Mode prédiction")
        parser.add_argument("-b", action="store_true", help="Regénérer base de données")
        parser.add_argument("-t", type=int, help="Taille de la fenetre")
        parser.add_argument("--encodage", type=str,default="utf-8", help="Encodage du fichier texte")
        parser.add_argument("--chemin", type=str, help="Chemin du fichier texte")
        argp = parser.parse_args()

        if sum([argp.e, argp.p, argp.b]) != 1:
            parser.error("Choisissez exactement un mode : -e, -p ou -b")
          
        if (argp.e or argp.p) and not argp.t:
            parser.error("-t est requis avec -e et -p")
        elif argp.t is not None and argp.t <= 0:
            parser.error("-t doit être un entier positif")

        if argp.e and argp.chemin is None:
            parser.error("--chemin est requis avec -e")

        #pas necessaire pour le format cli
        #parser.add_argument("-q", action="store_true", help="Quitter le programme")


        
        return argp
        
        #if(argp.b):

import argparse
from entrainement import Entrainement
from recherche import Recherche


class Argument_terminale():
    def run(self):
        parser = argparse.ArgumentParser(description = "Entrez un mot, le nombre de synonymes que vous voulez et la méthode de calcule, i.e. produit scalaire: 0, least-squares:1, city-block: 2\r\nTapez q pour quitter.\r\n")
        
        parser.add_argument("-e", "--entrainement", action="store_true", help="Mode entrainement")
        parser.add_argument("-p", "--prediction", action="store_true", help="Mode prédiction")
        

        parser.add_argument("-t", "--taille" , type=int, help="Taille de la fenetre")
        parser.add_argument("--encodage", type=str, help="Encodage du fichier texte")
        parser.add_argument("--chemin", type=str, help="Chemin du fichier texte")

        parser.add_argument("-b", "--bd", action="store_true", help="Regénérer base de données")

        parser.add_argument("-q", action="store_true", help="Quitter le programme")


        argp = parser.parse_args()
        return argp
        
        #if(argp.b):

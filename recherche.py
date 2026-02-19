#Trouver les Synonymes
import numpy as np
import re

class Recherche:
    def __init__(self,chemin,encodage,matrice,dictionnaire,commande_complete):
        self.text = self.creationTexte(self,chemin,encodage)



    def creationTexte(self,chemin,encodage):
        f = open(chemin, encoding=encodage)
        texte = f.read()
        texte = re.findall(r'\w+' , texte)
        texte_lower = [item.lower() for item in texte]
        f.close()
        return texte_lower

        
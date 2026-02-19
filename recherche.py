#Trouver les Synonymes
import numpy as np
import re

class recherche:
    def __init__(self,chemin,encodage):
        pass

    def creationTexte(self,chemin,encodage):
        f = open(chemin, encoding=encodage)
        texte = f.read()
        texte = re.findall(r'\w+' , texte)

        f.close()
        return texte

        
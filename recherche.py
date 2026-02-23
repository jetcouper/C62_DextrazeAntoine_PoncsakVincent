#Trouver les Synonymes
import numpy as np
import re

class Recherche:
    def __init__(self,chemin,encodage,matrice,dictionnaire,mot,nb_synonymes,methode):
        self.text = self.creationTexte(chemin,encodage)

        if methode == "0":
            self.scalaire(matrice, dictionnaire,mot,nb_synonymes)


    def creationTexte(self, chemin,encodage):
        f = open(chemin, encoding=encodage)
        texte = f.read()
        texte = re.findall(r'\w+' , texte)
        texte_lower = [item.lower() for item in texte]
        f.close()
        return texte_lower

    def scalaire(self,matrice, dictionnaire,mot,nb_synonymes):
        list_mot = []
        try:
            index_mot = dictionnaire[mot]
        except KeyError:
            print("Ce mot n'est pas présent dans le texte.")
        
        matrice_mot = matrice[index_mot]

        #mot_recherche = dictionnaire.
        for index, valeur in enumerate(matrice):
            if index != index_mot:
                pass
        
        pass
        
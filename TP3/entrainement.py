#Quant tu lis le texte et créer les deux structures
import numpy as np
from dao import BaseDeDonnees
import re

class Entrainement:
    def __init__(self, fenetre, bd):
        self.bd = bd
        self._matrice = None
        self._dict = None
        self.fenetre = fenetre
        
    @property
    def matrice(self):
        return self._matrice
    
    @matrice.setter
    def matrice(self,value):
        self._matrice = value
    
    @property
    def dictionnaire(self):
        return self._dict
    
    @matrice.setter
    def dictionnaire(self,value):
        self._dict = value

    def entrainer(self,chemin,encodage):
        texte = self.creationTexte(chemin,encodage)
        self._matrice, self._dict = self.creationMatrice(texte)
        self.miseAJourBD()

    def miseAJourBD(self):
        self.bd.inserer_mots(self.dict.items())
        liste_tuple = []
        for i, j in np.argwhere(self.matrice > 0):
            liste_tuple.append((int(i),int(j),self.fenetre,int(self.matrice[i,j])))
        self.bd.inserer_cooccurrences(liste_tuple)
    

    def creationMatrice(self, texte):
        mot_a_index = self.bd.charger_lexique()

        for mot in texte:
            if mot not in mot_a_index:
                mot_a_index[mot] = len(mot_a_index)

        size = len(mot_a_index)
        # Create the 2D array of zeros with integer data type
        zero_matrix = np.zeros((size,size), dtype=int)
        demi_fenetre = self.fenetre//2

        for index, mot_central in enumerate(texte):
            i = mot_a_index[mot_central]
            debut = max(0, index - demi_fenetre)
            fin = min(len(texte), index + demi_fenetre + 1)
            for indexVoisin in range(debut,fin):
                if indexVoisin != index:
                    voisin = texte[indexVoisin]
                    j = mot_a_index[voisin]
                    zero_matrix[i,j] += 1
        print("entrainement terminer")
        self.matrice = zero_matrix
        self.dict = mot_a_index
        return zero_matrix, mot_a_index
    
    def creationTexte(self,chemin,encodage):
        f = open(chemin, encoding=encodage)
        texte = f.read().lower()
        texte = re.findall(r'\w+' , texte)
        f.close()
        return texte
    
    def chargerBD(self,normaliser=False, conserver = 0):
        mot_a_index = self.bd.charger_lexique()
        matrice_coocurance = self.bd.charger_cooccurrences(self.fenetre)
        if conserver > 0:
            sommes = np.sum(matrice_coocurance, axis=0)
            indexes = np.argsort(sommes)[::-1][:conserver]
            m = np.zeros((len(matrice_coocurance), conserver))
            m[:] = matrice_coocurance[:, indexes][:]
            matrice_coocurance = m
        
        if normaliser:
            norm = np.linalg.norm(matrice_coocurance, axis = 1, keepdims=True)

            #equivalent d'une boucle for qui verify if 0 change pour 1
            norm[norm == 0] = 1

            matrice_coocurance = matrice_coocurance / norm
          
        return mot_a_index, matrice_coocurance





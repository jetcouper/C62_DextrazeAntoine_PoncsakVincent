#Trouver les Synonymes
import numpy as np
import re

class Recherche:
    def __init__(self,chemin,encodage,matrice,dictionnaire,mot,nb_synonymes,methode):
        self.text = self.creationTexte(chemin,encodage)
        self.resultat = {}
        if methode == "0":
            self.resultat = self.scalaire(matrice, dictionnaire,mot,nb_synonymes)
        elif methode == "1":
            pass
        elif methode == "2":
            pass


    def creationTexte(self, chemin,encodage):
        f = open(chemin, encoding=encodage)
        texte = f.read()
        texte = re.findall(r'\w+' , texte)
        texte_lower = [item.lower() for item in texte]
        f.close()
        return texte_lower

    def scalaire(self,matrice, dictionnaire,mot,nb_synonymes):
        list_mot_score = {}
        score = 0
        list_mot = list(dictionnaire.keys())
        nb_mot = int(nb_synonymes)
        try:
            index_mot = dictionnaire[mot]
        except KeyError:
            print("Ce mot n'est pas présent dans le texte.")
        
        matrice_mot = matrice[index_mot]
        tuple_matrice_mot = tuple(matrice_mot)
        #mot_recherche = dictionnaire.
        for index, valeur in enumerate(matrice):
            if index != index_mot:
                score = np.dot(matrice_mot,valeur)
                list_mot_score[list_mot[index]] = score
                pass
        
        liste_trier = dict(sorted(list_mot_score.items(), key= lambda item: item[1],reverse=True)[:nb_mot])
        return liste_trier
        pass
        
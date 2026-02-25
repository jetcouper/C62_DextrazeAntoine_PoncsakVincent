#Trouver les Synonymes
import numpy as np
import re

class Recherche:
    def __init__(self,chemin,encodage,matrice,dictionnaire,mot,nb_synonymes,methode):
        self.text = self.creationTexte(chemin,encodage)
        self.resultat = {}
        self.resultat = self.calcul(matrice, dictionnaire,mot,nb_synonymes,methode)

    def creationTexte(self, chemin,encodage):
        f = open(chemin, encoding=encodage)
        texte = f.read()
        texte = re.findall(r'\w+' , texte)
        texte_lower = [item.lower() for item in texte]
        f.close()
        return texte_lower

    def calcul(self,matrice, dictionnaire,mot,nb_synonymes,methode):
        list_mot_score = {}
        score = 0
        list_mot = list(dictionnaire.keys())
        nb_mot = int(nb_synonymes)
        try:
            index_mot = dictionnaire[mot]
        except KeyError:
            print("Ce mot n'est pas présent dans le texte.")
        
        matrice_mot = matrice[index_mot]
        
        for index, valeur in enumerate(matrice):
            if index != index_mot:
                if methode == "0":
                    #calcule scalaire
                    score = np.dot(matrice_mot,valeur)
                elif methode == "1":
                    #calcule moindre_carres
                    score = np.sum(np.square(matrice_mot - valeur))
                elif methode == "2":
                    #calcule city_block
                    score = np.sum(np.abs(matrice_mot - valeur))
                
                list_mot_score[list_mot[index]] = score
        if methode == "0":
            #maximiser résultat
            liste_trier = dict(sorted(list_mot_score.items(), key= lambda item: item[1],reverse=True)[:nb_mot])
        else:
            #minimiser le resultat
            liste_trier = dict(sorted(list_mot_score.items(), key= lambda item: item[1])[:nb_mot])   
        return liste_trier
    
    
    
    
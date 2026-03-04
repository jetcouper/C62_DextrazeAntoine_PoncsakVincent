#Quant tu lis le texte et créer les deux structures
import numpy as np
import re

class Entrainement:
    def __init__(self,chemin,encodage,fenetre):
        #word_list = ["apple", "banana", "cherry", "date"]
        #num_columns = 10 # Example: specify the desired number of columns

        # Define the shape of the 2D array using the length of the word list
        # Shape format is (rows, columns)
        self.matrice, self.dict = self.creationMatrice(self.creationTexte(chemin,encodage),fenetre)


        print("entrainement terminer")
    
    def creationMatrice(self, texte,fenetre):
        list_unique = []
        for i in texte:
            if i not in list_unique:
                list_unique.append(i)


        mot_a_index = {word: index for index, word in enumerate(list_unique)}
        size = len(list_unique)
        # Create the 2D array of zeros with integer data type
        zero_matrix = np.zeros((size,size), dtype=int)
        demi_fenetre = fenetre//2

        for index, mot_central in enumerate(texte):
            i = mot_a_index[mot_central]
            debut = max(0, index - demi_fenetre)
            fin = min(len(texte), index + demi_fenetre + 1)
            for indexVoisin in range(debut,fin):
                if indexVoisin != index:
                    voisin = texte[indexVoisin]
                    j = mot_a_index[voisin]
                    zero_matrix[i,j] += 1
        return zero_matrix, mot_a_index
    
    def creationTexte(self,chemin,encodage):
        f = open(chemin, encoding=encodage)
        texte = f.read()
        texte = re.findall(r'\w+' , texte)
        texte_lower = [item.lower() for item in texte]
        
            

        f.close()
        return texte_lower

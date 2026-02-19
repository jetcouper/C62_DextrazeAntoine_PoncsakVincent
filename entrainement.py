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
        list_mot_dic = {}
        list_unique = []
        list_mot = []
        for i in texte:
            if i not in list_unique:
                list_unique.append(i)
              
        for i in texte:
            list_mot.append(i)
        array_shape = (len(list_unique), len(list_unique))
        list_mot_dic = {index: string for index, string in enumerate(list_unique)}
        # Create the 2D array of zeros with integer data type
        zero_matrix = np.zeros(array_shape, dtype=int)

        # for index, string in list_mot_dic.items():
        #     for index2, string2 in list_mot_dic.items():
        #         if string != string2:
        # for string in list_mot:
        #      for string2 in list_mot:
                 
                 



        return zero_matrix, list_mot_dic
    
    def creationTexte(self,chemin,encodage):
        f = open(chemin, encoding=encodage)
        texte = f.read()
        texte = re.findall(r'\w+' , texte)

        f.close()
        return texte

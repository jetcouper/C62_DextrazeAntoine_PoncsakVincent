import random as rd
import numpy as np


class Clustering():
    def __init__(self, nb_k, matrice , lexique : dict[str, int]):
        self.__nb_k = nb_k
        self.__matrice = matrice
        self.__lexique = lexique
        self.liste_cluster : list
        self.liste_centroide : list[int] = [rd.randint(1,len(lexique)+1) for _ in range(nb_k)]
        pass


    def calculerCentroide(self):


        pass
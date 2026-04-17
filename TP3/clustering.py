import random as rd
import numpy as np


class Clustering():
    def __init__(self, nb_k, coocurance , lexique : dict[str, int]):
        self.__nb_k = nb_k
        self.__coocurance = coocurance
        self.__lexique = lexique
        self.matrice_mot = self.recreerMatriceMot()

        
        self.matrice_cluster = np.zeros(len(lexique), dtype=int)

        #self.matrice_centroide : np.ndarray = np.zeros((nb_k, len(lexique)))
        self.matrice_centroide : np.ndarray = np.array([self.matrice_mot[rd.randint(0, len(lexique)-1)] for i in range(nb_k)])
        self.assignerCluster()
        pass

    def recreerMatriceMot(self) -> np.ndarray:
        matrice_mot = np.zeros((len(self.__lexique), len(self.__lexique)), dtype=int)
        for tuples in self.__coocurance:
            mot1_id, mot2_id, compte = tuples
            matrice_mot[mot1_id][mot2_id] = compte
        return matrice_mot

    def calculerCentroide(self):
        pass

    def assignerCluster(self):
        for i in range(len(self.__lexique)):
            distances = np.sum(np.square(self.matrice_centroide - self.matrice_mot[i]), axis=1)
            self.matrice_cluster[i] = np.argmin(distances)
        pass
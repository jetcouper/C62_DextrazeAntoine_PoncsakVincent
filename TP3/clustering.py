import random as rd
import numpy as np
from time import perf_counter


class Clustering():
    def __init__(self, nb_k, coocurance , lexique : dict[str, int]):
        self.__nb_k = nb_k
        self.__coocurance = coocurance
        self.__lexique = lexique
        self.matrice_mot = self.recreerMatriceMot()

        self.matrice_cluster = np.zeros(len(lexique), dtype=int)
        
        self.indices = rd.sample(range(len(lexique)), self.__nb_k)
        self.matrice_centroide = np.array([self.matrice_mot[i] for i in self.indices])
        print("Première assignation de cluster")
        t = perf_counter()
        self.assignerCluster()
        print("Premier calcule de centoïde")
        self.calculerCentroide()
        print(f"\r\nChargement des données en {(perf_counter() - t):.2f} secondes")
        self.fit()
        
        pass

    def fit(self):
        print("Début des itérations")
        compteur = 0
        nb_migration = 0
        ancien_cluster = np.zeros(len(self.matrice_cluster), dtype=int)
        while not np.array_equal(ancien_cluster,self.matrice_cluster):
            t = perf_counter()
            nb_migration = np.sum(ancien_cluster != self.matrice_cluster)
            compteur += 1 
            ancien_cluster = self.matrice_cluster
            self.calculerCentroide()
            self.assignerCluster()
            print(f"\r\nItération {compteur} : {(perf_counter() - t):.2f} secondes")
            print(f"{nb_migration} migrations.")
            print("\r\n ************************ \r\n")
            for i in range(self.__nb_k):
                print(f"Partition {i} : {np.sum(self.matrice_cluster == i)} mots.")

        if np.array_equal(ancien_cluster,self.matrice_cluster):
            print(f"Arrêt après {compteur} itération")
    
    def recreerMatriceMot(self) -> np.ndarray:
        print("Recréation de matrice")
        matrice_mot = np.zeros((len(self.__lexique), len(self.__lexique)), dtype=int)
        for tuples in self.__coocurance:
            mot1_id, mot2_id, compte = tuples
            matrice_mot[mot1_id][mot2_id] = compte
        return matrice_mot

    def calculerCentroide(self):
        for k in range(self.__nb_k):
            mask = self.matrice_cluster == k
            if mask.any():
                self.matrice_centroide[k] = self.matrice_mot[mask].mean(axis=0)
        pass

    def assignerCluster(self):
        

        self.matrice_cluster = np.zeros(len(self.matrice_cluster), dtype=int)
        for i in range(len(self.__lexique)):
            # distances = np.sum(np.square(self.matrice_centroide - self.matrice_mot[i]), axis=1)
            # self.matrice_cluster[i] = np.argmin(distances)
            distance = [np.sum(np.square(c - self.matrice_mot[i])) for c in self.matrice_centroide]
            self.matrice_cluster[i] = distance.index(min(distance))
        pass
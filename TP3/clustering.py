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

        #Choice pour ne pas avoir la m^me ranger
        self.indices = rd.sample(range(len(lexique)), self.__nb_k)
        self.matrice_centroide = np.array([self.matrice_mot[i] for i in self.indices])
        #self.matrice_centroide : np.ndarray = np.array([self.matrice_mot[rd.randint(0, len(lexique)-1)] for i in range(self.__nb_k)])
        print("Première assignation de cluster")
        self.assignerCluster()
        print("Premier calcule de centoïde")
        self.calculerCentroide()
        self.fit(50)
        pass

    def fit(self, max_iter=100):
        print("Début des itérations")
        compteur = 0
        nb_migration = 0
        ancien_cluster = np.zeros(len(self.matrice_cluster), dtype=int)
        while not np.array_equal(ancien_cluster,self.matrice_cluster):
            nb_migration = np.sum(ancien_cluster != self.matrice_cluster)
            compteur += 1 
            ancien_cluster = self.matrice_cluster
            self.calculerCentroide()
            self.assignerCluster()
            print(f"\r\nItération {compteur}")
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
            mot_cluster = self.matrice_mot[self.matrice_cluster == k]
            if len(mot_cluster) > 0:
                self.matrice_centroide[k] = mot_cluster.mean(axis=0)
        pass

    def assignerCluster(self):
        self.matrice_cluster = np.zeros(len(self.matrice_cluster), dtype=int)
        for i in range(len(self.__lexique)):
            distances = np.sum(np.square(self.matrice_centroide - self.matrice_mot[i]), axis=1)
            self.matrice_cluster[i] = np.argmin(distances)
        pass
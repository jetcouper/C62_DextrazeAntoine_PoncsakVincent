import random as rd
import numpy as np
from time import perf_counter
from collections import defaultdict
import statistics


class Clustering():
    def __init__(self, nb_k, coocurance , lexique : dict[str, int]):
        self.__nb_k = nb_k
        self.__coocurance = coocurance
        self.__lexique = lexique
        self.matrice_mot = self.recreerMatriceMot()


        self.matrice_cluster = np.zeros(len(lexique), dtype=int)
        t = perf_counter()
        self.indices = rd.sample(range(len(lexique)), self.__nb_k)
        self.matrice_centroide = np.array([self.matrice_mot[i] for i in self.indices])
        print("Première assignation de cluster")
        t2 = perf_counter()
        self.assignerCluster()
        print("Premier calcule de centoïde")
        self.calculerCentroide()
        print(f"\r\nChargement des données en {(perf_counter() - t2):.2f} secondes")
        self.fit()
        print(f"Partitionnement en {(perf_counter() - t):.2f} secondes.")
        

        

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
            print(f"{nb_migration} migrations.\r\n")
            for i in range(self.__nb_k):
                print(f"Partition {i} : {np.sum(self.matrice_cluster == i)} mots.")
            print("\r\n************************\r\n")

        if np.array_equal(ancien_cluster,self.matrice_cluster):
            print(f"Arrêt après {compteur} itération")
    

    def recreerMatriceMot(self) -> np.ndarray:
        print("Recréation de matrice")
        matrice_mot = np.zeros((len(self.__lexique), len(self.__lexique)), dtype=float)
        for tuples in self.__coocurance:
            mot1_id, mot2_id, compte = tuples
            matrice_mot[mot1_id][mot2_id] = compte
        return matrice_mot

    def obtenirMotProche(self,lexique_inverse)->defaultdict[list]:
        
        partition = 0
        mots = defaultdict(list)

        for j in range(len(lexique_inverse)):
            partition = self.matrice_cluster[j]
            distance = np.sum(np.square(self.matrice_centroide[partition] - self.matrice_mot[j]))

            mots[partition].append((distance, lexique_inverse[j]))
        
        for p in mots:
            mots[p] = sorted(mots[p], key=lambda x : x[0], reverse=False)
        

        return mots

    def calculerCentroide(self):
        for k in range(self.__nb_k):
            mask = self.matrice_cluster == k
            if mask.any():
                self.matrice_centroide[k] = self.matrice_mot[mask].mean(axis=0)
        

    def assignerCluster(self):
        self.matrice_cluster = np.zeros(len(self.matrice_cluster), dtype=int)
        for i in range(len(self.__lexique)):
            distance = [np.sum(np.square(c - self.matrice_mot[i])) for c in self.matrice_centroide]
            self.matrice_cluster[i] = distance.index(min(distance))
        

    def retourneReponse(self, nombre_retour) -> dict:
        inverse = {v:k for k, v in self.__lexique.items()}
        mots = self.obtenirMotProche(inverse)

        for p in sorted(mots):
            print(f"Partition {p}:")
            for mot in mots[p][:nombre_retour]:
                print(f"\t{mot[1]} -> {float(mot[0]):.2f}")




        #for i in range(self.__nb_k):
        #    mots[i] = np.where(self.matrice_cluster == i)[0]

                

        
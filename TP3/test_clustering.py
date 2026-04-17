import numpy as np
import random as rd

# -------------------------------------------------------------------
# Matrice de co-occurrences fictive 5x5
# Mots : ["chat", "chien", "lapin", "voiture", "camion"]
# -------------------------------------------------------------------
lexique = {"chat": 0, "chien": 1, "lapin": 2, "voiture": 3, "camion": 4}
nb_mots = len(lexique)
nb_k = 2  # 2 clusters

matrice_mot = np.array([
    #chat  chien lapin voitu camion
    [  0,    8,    7,    1,    0  ],  # chat
    [  8,    0,    6,    0,    1  ],  # chien
    [  7,    6,    0,    1,    0  ],  # lapin
    [  1,    0,    1,    0,    9  ],  # voiture
    [  0,    1,    0,    9,    0  ],  # camion
], dtype=float)

print("=== Matrice de co-occurrences ===")
noms = list(lexique.keys())
print(f"{'':10}", end="")
for n in noms:
    print(f"{n:10}", end="")
print()
for i, n in enumerate(noms):
    print(f"{n:10}", end="")
    for val in matrice_mot[i]:
        print(f"{int(val):10}", end="")
    print()

# -------------------------------------------------------------------
# Initialisation des centroïdes (2 mots aléatoires)
# -------------------------------------------------------------------
indices = rd.sample(range(nb_mots), nb_k)
matrice_centroide = matrice_mot[indices].copy()
print(f"\n=== Centroides initiaux (indices {indices}) ===")
for i, idx in enumerate(indices):
    print(f"  Centroide {i} = vecteur de '{noms[idx]}' -> {matrice_centroide[i]}")

# -------------------------------------------------------------------
# Vecteur d'assignations (un numéro de cluster par mot)
# -------------------------------------------------------------------
matrice_cluster = np.zeros(nb_mots, dtype=int)

# -------------------------------------------------------------------
# Boucle K-means
# -------------------------------------------------------------------
for iteration in range(10):
    anciennes_assignations = matrice_cluster.copy()

    # --- Assignation ---
    for i in range(nb_mots):
        distances = np.sum(np.square(matrice_centroide - matrice_mot[i]), axis=1)
        matrice_cluster[i] = np.argmin(distances)

    print(f"\n--- Itération {iteration + 1} ---")
    print("  Assignations :", {noms[i]: int(matrice_cluster[i]) for i in range(nb_mots)})

    # --- Recalcul des centroïdes ---
    for k in range(nb_k):
        membres = np.where(matrice_cluster == k)[0]
        if len(membres) > 0:
            matrice_centroide[k] = np.mean(matrice_mot[membres], axis=0)
            print(f"  Centroide {k} recalcule depuis {[noms[m] for m in membres]} -> {matrice_centroide[k]}")

    # --- Convergence ---
    if np.array_equal(matrice_cluster, anciennes_assignations):
        print(f"\n  Convergence atteinte à l'itération {iteration + 1}.")
        break

# -------------------------------------------------------------------
# Résultat final
# -------------------------------------------------------------------
print("\n=== Résultat final ===")
for k in range(nb_k):
    membres = [noms[i] for i in range(nb_mots) if matrice_cluster[i] == k]
    print(f"  Cluster {k} : {membres}")

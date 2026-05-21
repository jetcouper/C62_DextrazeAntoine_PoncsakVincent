# TP - Clustering K-means

Par Antoine Dextraze et Vincent Poncsak.

## Prérequis

- Python 3.13+
- NumPy
- Matplotlib

## Base de données

La BD (`cooccurrences.db`) est déjà entraînée sur les quatre textes suivants avec une fenêtre de taille 5 :

- Don Quichotte
- Germinal
- Le Ventre de Paris
- Les Trois Mousquetaires

Aucun ré-entraînement nécessaire au lancement.

## Configurations testées

### Configuration de base

```
python main.py -c -t 5 -k 5 -n 10
```

### Avec normalisation

```
python main.py -c -t 5 -k 5 -n 10 --normaliser
```

### Avec conservation de features (20 000 colonnes)

```
python main.py -c -t 5 -k 5 -n 10 --conserver 20000
```

### Avec normalisation et conservation

```
python main.py -c -t 5 -k 5 -n 10 --normaliser --conserver 20000
```

### Avec graphe des migrations

```
python main.py -c -t 5 -k 5 -n 10 --graphe
```

### Redirection des résultats

```
set PYTHONIOENCODING=utf-8
python main.py -c -t 5 -k 5 -n 10 > resultats_t5_k5.txt
```

## Fonctionnalités TP2 (toujours opérationnelles)

### Entraînement

```
python main.py -e -t 5 --chemin textes/GerminalUTF8.txt
```

### Prédiction de synonymes

```
python main.py -p -t 5
```

### Régénérer la base de données

```
python main.py -b
```

## Arguments disponibles

| Argument                 | Description                                      |
| ------------------------ | ------------------------------------------------ |
| `-c`                   | Mode clustering                                  |
| `-e`                   | Mode entraînement                               |
| `-p`                   | Mode prédiction                                 |
| `-b`                   | Régénérer la base de données                 |
| `-t <taille>`          | Taille de la fenêtre de cooccurrences           |
| `-k <nombre>`          | Nombre de centroïdes                            |
| `-n <nombre>`          | Nombre de mots à afficher par cluster           |
| `--normaliser`         | Normaliser la matrice avant le clustering        |
| `--conserver <nombre>` | Conserver les N colonnes les plus représentées |
| `--graphe`             | Afficher le graphe des migrations par itération |
| `--encodage <enc>`     | Encodage du fichier texte (défaut: utf-8)       |
| `--chemin <path>`      | Chemin du fichier texte (requis avec `-e`)     |

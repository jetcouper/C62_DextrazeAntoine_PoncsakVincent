import sqlite3
import numpy as np

CHEMIN_BD = "cooccurrences.db"

CREER_LEXIQUE = '''
CREATE TABLE IF NOT EXISTS lexique (
    id  INTEGER PRIMARY KEY,
    mot TEXT NOT NULL UNIQUE
)
'''
DROP_LEXIQUE = 'DROP TABLE IF EXISTS lexique'
INSERT_MOT = 'INSERT OR IGNORE INTO lexique (mot, id) VALUES (?, ?)'

CREER_COOCCURRENCES = '''
CREATE TABLE IF NOT EXISTS cooccurrences (
    mot1_id INTEGER,
    mot2_id INTEGER,
    fenetre INTEGER,
    compte  INTEGER NOT NULL,
    PRIMARY KEY (mot1_id, mot2_id, fenetre),
    FOREIGN KEY (mot1_id) REFERENCES lexique(id),
    FOREIGN KEY (mot2_id) REFERENCES lexique(id)
)
'''
DROP_COOCCURRENCES  = 'DROP TABLE IF EXISTS cooccurrences'
INSERT_COOCCURRENCE = '''
    INSERT INTO cooccurrences (mot1_id, mot2_id, fenetre, compte)
    VALUES (?, ?, ?, ?)
    ON CONFLICT(mot1_id, mot2_id, fenetre) DO UPDATE SET compte = compte + excluded.compte
'''

SELECT_LEXIQUE       = 'SELECT mot, id FROM lexique'
SELECT_COOCCURRENCES = 'SELECT mot1_id, mot2_id, compte FROM cooccurrences WHERE fenetre = ?'


class BaseDeDonnees:
    def __init__(self):
        self.connexion = None
        self.curseur   = None

    def __enter__(self):
        self.connexion = sqlite3.connect(CHEMIN_BD)
        self.curseur   = self.connexion.cursor()
        self.curseur.execute('PRAGMA foreign_keys = 1')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.curseur.close()
        self.connexion.close()
        self.connexion = None
        self.curseur   = None
        return False

    def creer_tables(self):
        self.curseur.execute(CREER_LEXIQUE)
        self.curseur.execute(CREER_COOCCURRENCES)
        self.connexion.commit()

    def detruire_tables(self):
        self.curseur.execute(DROP_COOCCURRENCES)
        self.curseur.execute(DROP_LEXIQUE)
        self.connexion.commit()

    def regenerer(self):
        self.detruire_tables()
        self.creer_tables()

    def inserer_mots(self, mots: list):
        self.curseur.executemany(INSERT_MOT, mots)
        self.connexion.commit()
    
    def inserer_cooccurrences(self, paires: list):
        self.curseur.executemany(INSERT_COOCCURRENCE, paires)
        self.connexion.commit()

    def charger_lexique(self) -> dict:
        self.curseur.execute(SELECT_LEXIQUE)
        return {mot: id_ for mot, id_ in self.curseur.fetchall()}

    def charger_cooccurrences(self, fenetre: int) -> np.ndarray:
        taille = len(self.charger_lexique())
        self.curseur.execute(SELECT_COOCCURRENCES, (fenetre,))
        matrice_mot = np.zeros((taille, taille))
        for mot1_id, mot2_id, compte in self.curseur.fetchall():
            matrice_mot[mot1_id][mot2_id] = compte
        return matrice_mot


        #return self.curseur.fetchall()
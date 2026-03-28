import sqlite3

CHEMIN_BD = "cooccurrences.db"

CREER_LEXIQUE = '''
CREATE TABLE IF NOT EXISTS lexique (
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    mot TEXT NOT NULL UNIQUE
)
'''
DROP_LEXIQUE = 'DROP TABLE IF EXISTS lexique'
INSERT_MOT   = 'INSERT INTO lexique (mot) VALUES (?)'

CREER_COOCCURRENCES = '''
CREATE TABLE IF NOT EXISTS cooccurrences (
    mot1_id INTEGER,
    mot2_id INTEGER,
    fenetre INTEGER,
    compte  INTEGER NOT NULL DEFAULT 1,
    PRIMARY KEY (mot1_id, mot2_id, fenetre),
    FOREIGN KEY (mot1_id) REFERENCES lexique(id),
    FOREIGN KEY (mot2_id) REFERENCES lexique(id)
)
'''
DROP_COOCCURRENCES  = 'DROP TABLE IF EXISTS cooccurrences'
INSERT_COOCCURRENCE = '''
    INSERT INTO cooccurrences (mot1_id, mot2_id, fenetre, compte)
    VALUES (?, ?, ?, ?)
'''

SELECT_LEXIQUE       = 'SELECT mot, id FROM lexique'
SELECT_COOCCURRENCES = 'SELECT mot1_id, mot2_id, compte FROM cooccurrences WHERE fenetre = ?'


class BaseDeDonnees:
    def __init__(self):
        self.connexion = None
        self.curseur   = None

    def connecter(self):
        self.connexion = sqlite3.connect(CHEMIN_BD)
        self.curseur   = self.connexion.cursor()
        self.curseur.execute('PRAGMA foreign_keys = 1')

    def deconnecter(self):
        self.curseur.close()
        self.connexion.close()
        self.connexion = None
        self.curseur   = None

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
        self.curseur.executemany(INSERT_MOT, [(mot,) for mot in mots])
    
    def inserer_cooccurrences(self, paires: list):
        self.curseur.executemany(INSERT_COOCCURRENCE, paires)

    def charger_lexique(self) -> dict:
        self.curseur.execute(SELECT_LEXIQUE)
        return {mot: id_ for mot, id_ in self.curseur.fetchall()}

    def charger_cooccurrences(self, fenetre: int) -> list:
        self.curseur.execute(SELECT_COOCCURRENCES, (fenetre,))
        return self.curseur.fetchall()
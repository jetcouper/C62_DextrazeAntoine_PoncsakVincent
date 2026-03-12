import sqlite3

CHEMIN_BD = "emp_dept.db"

CREER_DEPT = '''
CREATE TABLE IF NOT EXISTS dept 
(
    id  INTEGER PRIMARY KEY NOT NULL,
    nom CHAR(15) NOT NULL
)
'''

DROP_DEPT = '''
DROP TABLE IF EXISTS dept
'''

INSERT_DEPT = '''
INSERT INTO dept VALUES(?,?)
'''


CREER_EMP = '''
CREATE TABLE IF NOT EXISTS emp 
(
    id      INTEGER NOT NULL,
    nom     CHAR(15) NOT NULL,
    id_dept INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_dept) REFERENCES dept(id)
)
'''
DROP_EMP = '''
DROP TABLE IF EXISTS emp
'''

INSERT_EMP = '''
INSERT INTO emp(nom,id,id_dept) VALUES(?,?,?)
'''


# connexion = sqlite3.connect(CHEMIN_BD)

# curseur = connexion.cursor()
# curseur.execute("SELECT 'Hello world!!'")

# range = curseur.fetchall()

# for ranger in range:
#     print(ranger)

def connecter(chemin_bd = CHEMIN_BD):
    connexion = sqlite3.connect(chemin_bd)
    curseur = connexion.cursor()
    curseur.execute("PRAGMA foreign_keys = 1")

    return connexion, curseur

def deconnecter(connexion, curseur):
    curseur.close()
    connexion.close()


def creer_tables(curseur):
    curseur.execute(DROP_EMP)
    curseur.execute(DROP_DEPT)
    curseur.execute(CREER_DEPT)
    curseur.execute(CREER_EMP)

def inserer_données(connexion,curseur):
    curseur.execute(INSERT_DEPT, (1, "Informatique"))

    curseur.execute(INSERT_EMP, ("Marcel",1000,1))
    curseur.execute(INSERT_EMP, ("Michelle", 2000,1))
    curseur.execute(INSERT_EMP, ("Richard", 3000,1))
    curseur.execute(INSERT_EMP, ("Toto", 4000,1))

    nouveau_employé = [("Eric", 5000, 1), ("Jean-Marc", 6000, 1)]
    curseur.executemany(INSERT_EMP, nouveau_employé)

    connexion.commit()


def afficher_tables(curseur):
    print("\n------------DEPT--------------\n")
    curseur.execute("SELECT * FROM dept")
    for ranger in curseur.fetchall():
        print(ranger)
    print("\n------------EMP--------------\n")
    curseur.execute("SELECT * FROM emp")
    for ranger in curseur.fetchall():
        print(ranger)




def main():
    #Connecter au DAO
    connexion, curseur = connecter()
    #creer_tables(curseur)
    #inserer_données(connexion, curseur)
    afficher_tables(curseur)

    #curseur.execute("DELETE FROM emp WHERE nom = ?", ("Toto",))
    #afficher_tables(curseur)

    #curseur.execute("DELETE FROM dept")
    #afficher_tables(curseur)
    deconnecter(connexion, curseur)
    return 0

if __name__ == "__main__":    
    quit(main())
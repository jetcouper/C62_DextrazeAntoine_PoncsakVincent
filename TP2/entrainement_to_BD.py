from dao import BaseDeDonnees



class Entrainement_BD:
    def __init__(self):
        #self.BD = BaseDeDonnees()
        pass

    
    def insertion_mots(self, mots: list):
        with BaseDeDonnees() as bd:
            bd.inserer_mots(mots)

    def insertion_coocurrences(self,paires:list):
        with BaseDeDonnees() as bd:
            bd.inserer_cooccurrences(paires)
    
    def chargement_lexique(self) -> dict:
        with BaseDeDonnees() as bd:
            return bd.charger_lexique()
    
    def chargement_coocurrences(self, fenetre: int) -> list:
        with BaseDeDonnees() as bd:
            return bd.charger_cooccurrences(fenetre)

#Trouver les Synonymes
import numpy as np
import re

class Recherche:
    def __init__(self):
        pass
        
    def recherche(self, matrice,dictionnaire,mot,nb_synonymes,methode) -> dict:
        matrice_refait = matrice
        

        return self.calcul(matrice_refait, dictionnaire,mot,int(nb_synonymes),int(methode))

    def creationTexte(self, chemin,encodage):
        f = open(chemin, encoding=encodage)
        texte = f.read()
        texte = re.findall(r'\w+' , texte)
        texte_lower = [item.lower() for item in texte]
        f.close()
        return texte_lower

    def stopwords(self):
        list_stop = []
        stop_words = "où qu je tu il ils nous vous le la les un une des mon ton son nôtres notre vôtres votre leur leurs mes tes ces ses nos vos au aux avec ce dans de du elle en et eux lui ma mais me même moi ne on ou par pas pour qu' que qui sa se sur ta te toi ceci cela cet cette ici quel quels quelle quelles sans soi ainsi alors car comme donc lorsque puisque quoique si sinon tandis toutefois or ni voire aussi bien déjà encore jamais moins toujours très trop assez autant ailleurs alors après avant hier demain souvent parfois vite tard tôt ainsi presque aucun aucune certain certaine certains certaines chaque plusieurs quelconque tout toute tous toutes a b c d e f g h i j k l m n o p q r s t u v w x y z à â ä æ ç é è ê ë î ï ô ö œ ù û ü ÿ À Â Ä Æ Ç É È Ê Ë Î Ï Ô Ö Œ Ù Û Ü Ÿ"
        list_stop = stop_words.split()
        return list_stop


    def calcul(self,matrice, dictionnaire,mot,nb_synonymes,methode):
        list_mot_score = {}
        score = 0
        list_mot = list(dictionnaire.keys())
        nb_mot = int(nb_synonymes)

        if mot not in dictionnaire:
            raise Exception("Ce mot n'est pas dans le texte")
        
        index_mot = dictionnaire[mot]
        matrice_mot = matrice[index_mot]
        
        for index, valeur in enumerate(matrice):
            if index != index_mot:
                if methode == 0:
                    #calcule scalaire
                    score = np.dot(matrice_mot,valeur)
                elif methode == 1:
                    #calcule moindre_carres
                    score = np.sum(np.square(matrice_mot - valeur))
                elif methode == 2:
                    #calcule city_block
                    score = np.sum(np.abs(matrice_mot - valeur))
                
                list_mot_score[list_mot[index]] = score
        liste_stopword = self.stopwords()
        for i in liste_stopword:
            if i in list_mot_score:
                del list_mot_score[i]
        if methode == 0:
            #maximiser résultat
            liste_trier = dict(sorted(list_mot_score.items(), key= lambda item: item[1],reverse=True)[:nb_mot])
        else:
            #minimiser le resultat
            liste_trier = dict(sorted(list_mot_score.items(), key= lambda item: item[1])[:nb_mot])   
        return liste_trier
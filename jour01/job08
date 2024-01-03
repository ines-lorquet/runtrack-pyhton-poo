from math import *
class Cercle:
    def __init__(self, rayon):
        self.donner_rayon = rayon
    
    def changerRayon(self,n_rayon):
        self.donner_rayon = n_rayon
        return n_rayon

    def afficherInfos(self):
        print("Rayon :", self.donner_rayon)
        print("Circonférence :", self.circonference())
        print("Aire :", self.aire())
        print("Diamètre :", self.diametre() )
        
    def circonference(self):
        a = self.donner_rayon
        resultat = a * 2 *pi
        return resultat

    def aire(self):
        rayon_carre = self.donner_rayon * self.donner_rayon * pi
        return rayon_carre

    def diametre(self):
        diam=self.donner_rayon + self.donner_rayon
        return diam
    
cercle1 = Cercle(4)
cercle1.afficherInfos()

cercle2 = Cercle(7)
cercle2.changerRayon(7)
cercle2.afficherInfos()
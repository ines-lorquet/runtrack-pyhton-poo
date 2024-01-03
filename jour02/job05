class Voiture:
    def __init__(self,marque,modele,annee,kilometrage,en_marche,reservoir):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir
    def get_marque(self):
        return self.__marque
    def set_marque(self,marque):
        self.__marque = marque
    def get_modele(self):
        return self.__modele
    def set_modele(self,modele):
        self.__modele = modele
    def get_annee(self):
        return self.__annee
    def set_annee(self,annee):
        self.__annee = annee
    def get_kilometrage(self):
        return self.__kilometrage
    def set_kilometrage(self,kilometrage):
        self.__kilometrage = kilometrage
    def get_en_marche(self):
        return self.__en_marche
    def set_en_marche(self,en_marche):
        self.__en_marche = en_marche
    def get_reservoir(self):
        return self.__reservoir
    def set_reservoir(self,reservoir):
        self.__reservoir = reservoir
    
    def demarrer(self):
        if self.__verifier_plein()>5:
            self.set_en_marche(True)
            return "la voiture avanceee vrooomm"
    def arreter(self):
        self.set_en_marche(False)
    def __verifier_plein(self):
        return self.get_reservoir()
    
voiture1 = Voiture("Ferrari","F40",1987,100000,False,50)
print(voiture1.demarrer())
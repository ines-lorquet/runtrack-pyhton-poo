class Animal:
    def __init__(self,age,prenom):
        self.animal_age = age
        self.animal_prenom = prenom
        
    def vieillir(self):
        self.animal_age +=1
        print("L'âge de l'animal",self.animal_age,"ans")
        
    def nommer(self,prenom):
        print("L'animal se nomme",prenom)

afficher_age = Animal(0,"")
afficher_age.vieillir()

afficher_prenom = Animal(0,"")
afficher_prenom.nommer("Luna")


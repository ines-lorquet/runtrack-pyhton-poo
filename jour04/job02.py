class Personne:
    def __init__(self):
        self.age = 14
        
    def get_age(self):
        return self.age
    
    def set_age(self,age):
        self.age = age
        
    def afficherAge(self):
        print(f"Age : {self.get_age()}")
        
    def bonjour(self):
        print("Hello")
        
    def modifierAge(self,entier):
        if entier == int:
            self.set_age(entier)
        else:
            print("L'âge rentré n'est pas un entier" )
        
class Eleve(Personne):
        
    def allerEnCours(self):
        print("Je vais en cours")
        
    def afficherAge(self):
        print(f"J'ai {self.get_age()}ans")
        
class Professeur:
    def __init__(self,matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee
    def enseigner(self):
        print("Le cours va commercer")
    
eleve1 = Eleve()
personne1 = Personne()
professeur1 = Professeur("Anglais")

personne1.afficherAge()

personne1.bonjour()
eleve1.allerEnCours()
personne1.modifierAge(15)
personne1.afficherAge()

professeur1.enseigner()
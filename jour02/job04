class Student:
    def __init__(self,nom,prenom,nb_etudiant,nb_credit):
        self.__nom = nom
        self.__prenom = prenom
        self.__nb_etudiant = nb_etudiant
        self.__nb_credit = nb_credit
        self.__level = self.__studentEval()
        
    def get_nom(self):
        return self.__nom
    def get_prenom(self):
        return self.__prenom    
    def get_nb_etudiant(self):
        return self.__nb_etudiant
    def get_level(self):
        return self.__level
    
    def get_nb_credit(self):
        return self.__nb_credit
    
    def credit_total(self):
        return f"""
    Le nombre de crédit de {self.__nom} est de {self.get_nb_credit()} point."""

    def set_nb_credit(self,nb_credit):
        if nb_credit > 0:
            self.__nb_credit += nb_credit

    def add_credits(self):
        self.set_nb_credit(10)

    def __studentEval(self):
        if self.get_nb_credit()>=90:
            return "Excellent"
        elif self.get_nb_credit()>=80:
            return "Très Bien"
        elif self.get_nb_credit()>=70:
            return "Bien"
        elif self.get_nb_credit()>=60:
            return "Passable"
        elif self.get_nb_credit()<60:
            return "Insuffisant"
        
    def studentInfo(self):
        return f"""
    Nom = {self.get_nom()} 
    Prénom = {self.get_prenom()}
    ID = {self.get_nb_etudiant()}
    Niveau = {self.get_level()}
    """

etudiant1 = Student("Doe","John",145,0)
etudiant1.add_credits()
etudiant1.add_credits()
etudiant1.add_credits()
print(etudiant1.credit_total())
print(etudiant1.studentInfo())
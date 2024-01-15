class Livre:
    def __init__(self,disponible):
        self.__disponible = disponible
        
    def get_disponible(self):
        return self.__disponible
    def set_disponible(self,disponible):
        self.__disponible = disponible
    
    def verification(self):
        if self.get_disponible() == True:
            print(self.get_disponible())
        else:
            print(self.get_disponible())

    def emprunter(self):
        if self.get_disponible()==True:
            self.__disponible = False
    
    def rendre(self):
        if self.get_disponible()==False:
            self.set_disponible(True) 

livre1 = Livre(True)
livre1.verification()
livre1.emprunter()
livre1.rendre()

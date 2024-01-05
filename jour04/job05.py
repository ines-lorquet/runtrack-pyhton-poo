class Forme:
    def aire(self):
        return 0
    
    
class Rectangle(Forme):
    def __init__(self,hauteur,largeur):
        self.hauteur = hauteur
        self.largeur = largeur
        
    def get_hauteur(self):
        return self.hauteur
    
    def get_largeur(self):
        return self.largeur
    
    def aire(self):
        rectangle = self.get_hauteur() * self.get_largeur()
        return rectangle
    
    
class Cercle(Forme):
    def __init__(self,radius):
        self.radius = radius
        
    def get_radius(self):
        return self.radius
    
    def aire(self):
        aire = 3.14 *(self.get_radius()*self.get_radius())
        return aire

cercle1 = Cercle(10)
print(cercle1.aire())

rectangle1 = Rectangle(10,20)
print(rectangle1.aire())

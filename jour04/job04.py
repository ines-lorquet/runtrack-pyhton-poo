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

rectangle1 = Rectangle(10,20)
print(rectangle1.aire())
        
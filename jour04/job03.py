class Rectangle:
    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur
    def set_longueur(self,longueur):
        self.__longueur = longueur
        
    def get_largeur(self):
        return self.__largeur
    def set_largeur(self,largeur):
        self.__largeur = largeur
        
    def perimetre(self):
        perimetre = (self.get_longueur() + self.get_largeur()) * 2
        return perimetre
        
    def surface(self):
        surface = self.get_longueur() * self.get_largeur()
        return surface
    
class Parrallelepipede(Rectangle):
    def __init__(self,hauteur,longueur,largeur):
        Rectangle.__init__(self,longueur,largeur)
        self.hauteur = hauteur

    def get_hauteur(self):
        return self.hauteur

    def volume(self):
        volume = self.get_longueur()*self.get_largeur()*self.get_hauteur()
        return volume

rectangle1 = Rectangle(10,20)
parrallelepipede1 = Parrallelepipede(3,10,20)

print(rectangle1.perimetre())
print(rectangle1.surface())
print(parrallelepipede1.volume())
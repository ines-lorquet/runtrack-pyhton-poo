class Livre:
    def __init__(self,titre,auteur,nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        
    def get_titre(self):
        return self.__titre
    def set_titre(self,titre):
        self.__titre = titre
        
    def get_auteur(self):
        return self.__auteur
    def set_auteur(self,auteur):
        self.__auteur = auteur
    
    def get_nb_pages(self):
        return self.__nb_pages 
    
    def set_nb_pages(self,nb_pages):
        if nb_pages <= 0 and nb_pages !=int:
            print("ERREUR : le nombre de page entré est négatif")
        else:
            self.__nb_pages = nb_pages
            
livre1= Livre("Histoire","Jean Claudine",12)
livre1.set_titre("Tragédie à Paris")
print(livre1.get_titre())
livre1.set_auteur("Joris Ballo")
print(livre1.get_auteur())
livre1.set_nb_pages(70)
print(livre1.get_nb_pages())


livre2= Livre("","",50)
livre2.set_titre("Boulevard du tueur")
print(livre2.get_titre())
livre2.set_auteur("Jeannette")
print(livre2.get_auteur())
livre2.set_nb_pages(-4)


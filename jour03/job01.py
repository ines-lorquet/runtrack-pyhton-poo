class Ville:
    def __init__(self, nom, nb_habitant):
        self.__nom = nom
        self.__nb_habitant = nb_habitant

    def get_nb_habitant(self):
        return self.__nb_habitant

    def set_nb_habitant(self, nb_habitant):
        self.__nb_habitant = nb_habitant

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

class Personne:
    def __init__(self, prenom, age, obj_ville):
        self.__prenom = prenom
        self.__age = age
        self.__obj_ville = obj_ville

    def get_prenom(self):
        return self.__prenom

    def get_obj_ville(self):
        return self.__obj_ville

    def set_obj_ville(self, obj_ville):
        self.__obj_ville = obj_ville

    def ajouterPopulation(self):
        maj_population = self.__obj_ville.get_nb_habitant()
        self.__obj_ville.set_nb_habitant(maj_population + 1)

ville1 = Ville("Paris", 1000000)
print("Population de la ville de", ville1.get_nom(), ":", ville1.get_nb_habitant(), "habitants")

ville2 = Ville("Marseille", 861635)
print("Population de la ville de", ville2.get_nom(), ":", ville2.get_nb_habitant(), "habitants")

personne1 = Personne("John", 45, ville1)
personne2 = Personne("Myrtille", 4, ville1)
personne3 = Personne("Chloé", 18, ville2)

personne1.ajouterPopulation()
personne2.ajouterPopulation()
personne3.ajouterPopulation()

print("Mise à Jour de la Population de la ville de", ville1.get_nom(), ":", ville1.get_nb_habitant(), "habitants")
print("Mise à Jour de la Population de la ville de", ville2.get_nom(), ":", ville2.get_nb_habitant(), "habitants")

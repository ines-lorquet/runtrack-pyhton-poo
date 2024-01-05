class Vehicule:
    def __init__(self,marque,modele,annee,prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
        
    def get_marque(self):
        return self.marque
    def get_modele(self):
        return self.modele
    def get_annee(self):
        return self.annee
    def get_prix(self):
        return self.prix
    
    def informationsVehicule(self):
        print(f"La Marque : {self.get_marque()}")
        print(f"Le Modèle : {self.get_modele()}")
        print(f"L'année : {self.get_annee()}")
        print(f"Le Prix : {self.get_prix()}")
        
    def demarrer(self):
        print("Attention je roule")
        
        
class Voiture(Vehicule):
    def __init__(self,marque,modele,annee,prix):
        Vehicule.__init__(self,marque,modele,annee,prix)
        self.portes = 4
        
    def get_portes(self):
        return self.portes
    
    def informationsVehicule(self):
        print(f"La Marque : {self.get_marque()}")
        print(f"Le Modèle : {self.get_modele()}")
        print(f"L'année : {self.get_annee()}")
        print(f"Le Prix : {self.get_prix()}")
        print(f"Nombres Portes : {self.get_portes()}")

    def demarrer(self):
        print("Attention je fais des drifts")
        
        
class Moto(Vehicule):
    def __init__(self,marque,modele,annee,prix):
        Vehicule.__init__(self,marque,modele,annee,prix)
        self.roue = 2
        
    def get_roue(self):
        return self.roue
    
    def informationsVehicule(self):
        print(f"La Marque : {self.get_marque()}")
        print(f"Le Modèle : {self.get_modele()}")
        print(f"L'année : {self.get_annee()}")
        print(f"Le Prix : {self.get_prix()}")
        print(f"Nombre de roue : {self.get_roue()}")
        
    def demarrer(self):
        print("Attention je fais un weeling")
        
        
voiture = Voiture("Mercedes","Classe A","2020",18500)
voiture.informationsVehicule()
voiture.demarrer()

moto = Moto("Yamaha","1200 Vmax", 1987,4500)
moto.informationsVehicule()


moto.demarrer()

class Produit:
    def __init__(self,nom,prixHT,TVA):
        self.nom_produit = nom
        self.prixHT_produit = prixHT
        self.TVA_produit = TVA

    def CalculerPrixTTC(self):
        prix_taxe =self.prixHT_produit+self.prixHT_produit*self.TVA_produit
        return prix_taxe
    
    def afficher(self):
        self.CalculerPrixTTC()
        return f"""
    Nom : {self.nom_produit}
    Prix Hors Taxe : {self.prixHT_produit} 
    Taxe : {self.TVA_produit}
    Prix avec taxe : {self.CalculerPrixTTC()}

"""

produit1 = Produit("Tongue",10,0.28)
print(produit1.afficher())

produit1 = Produit("Ordinateur",980,0.28)
print(produit1.afficher())



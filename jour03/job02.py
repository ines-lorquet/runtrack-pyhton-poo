class CompteBancaire:
    def __init__(self,nb_compte,nom,prenom,solde,decouvert):
        self.__nb_compte = nb_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    def get_nb_compte(self):
        return self.__nb_compte
    def set_nb_compte(self,nb_compte):
        self.__nb_compte = nb_compte
    def get_nom(self):
        return self.__nom
    def get_prenom(self):
        return self.__prenom
    def get_solde(self):
        return self.__solde
    def set_solde(self,solde):
        self.__solde = solde
    def get_decouvert(self):
        return self.__decouvert
    def set_decouvert(self,decouvert):
        self.__decouvert = decouvert
        
    def afficher(self):
        return f"""
    Nombre du Compte : {self.get_nb_compte()}
    Nom : {self.get_nom()}
    Prenom : {self.get_prenom()}
    Solde : {self.get_solde()} 
    """

    def afficherSolde(self):
        return f"""Afficher solde du compte{self.get_nb_compte()}: {self.get_solde()}"""
    
    def versement(self,verse):
        self.set_solde(self.get_solde()+verse)
        return self.get_solde()
        
    def retrait(self,nb_retrait):
        if self.get_decouvert() < nb_retrait:
            if self.get_decouvert ==True:
                self.set_solde(self.get_solde()-nb_retrait)
            else:
                return "Le retrait n'a pas était autorisé"
        else:
            self.set_solde(self.get_solde()-nb_retrait)
        return self.get_solde()
    
    def agios(self):
        if self.get_solde() < 0:
            agios = self.get_solde()+self.get_solde()*0.20
            self.set_solde(agios)
            return self.get_solde()
        else:
            pass

    def virement(self,ref,compte,montant):
        if self.get_solde() >= 0:
            self.retrait(montant)
            compte.versement(montant)
            return f"""
    Message : {ref}
    Vers le compte : {compte.get_nb_compte()}
    Montant : {montant} 
        """
        else:
            return """Erreur : virement impossible"""

        
compte1 = CompteBancaire(1,"Durand","Jean",10000,True)
print(compte1.afficher())
print(compte1.afficherSolde())
print(compte1.versement(3000))
print(compte1.retrait(2000))
print(compte1.agios())

compte2 = CompteBancaire(2,"Fosse","Michel",-200,True)
print(compte2.afficher())
print(compte2.afficherSolde())
print(compte1.virement("Evite le découvert",compte2,200))
print(compte2.afficherSolde())
class Joueur:
    def __init__(self,nom,numero,position):
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__nb_but = 0
        self.__passe_decisive = 0
        self.__cart_jaune = 0
        self.__cart_rouge = 0

    def get_nom(self):
        return self.__nom
        
    def get_numero(self):
        return self.__numero
        
    def get_position(self):
        return self.__position
        
    def get_nb_but(self):
        return self.__nb_but
    def set_nb_but(self,nb_but):
        self.__nb_but = nb_but
        
    def get_passe_decisive(self):
        return self.__passe_decisive
    def set_passe_decisive(self,passe_decisive):
        self.__passe_decisive = passe_decisive
        
    def get_cart_jaune(self):
        return self.__cart_jaune
    def set_cart_jaune(self,cart_jaune):
        self.__cart_jaune = cart_jaune
        
    def get_cart_rouge(self):
        return self.__cart_rouge
    def set_cart_rouge(self,cart_rouge):
        self.__cart_rouge= cart_rouge
        
    def marquerUnBut(self):
        self.set_nb_but(self.get_nb_but() + 1)
        print(f"Le Joueur {self.get_nom()} a marqué un but")
        
    def effectuerUnePasseDecisive(self):
        self.set_passe_decisive(self.get_passe_decisive() + 1)
        print(f"Le Joueur {self.get_nom()} a effectué une passe décisive")
        
    def recevoirUnCartonJaune(self):
        self.set_cart_jaune(self.get_cart_jaune() + 1)
        print(f"Le Joueur {self.get_nom()} a reçu un carton jaune")
        
    
    def recevoirUnCartonRouge(self):
        self.set_cart_rouge(self.get_cart_rouge() + 1)
        print(f"Le Joueur {self.get_nom()} a reçu un carton rouge")    
        
    def afficherStatistique(self):
        print(f"""
Nom joueur : {self.get_nom()}
Numéro joueur : {self.get_numero()}
But marquer : {self.get_nb_but()}
Passe décisive effectué : {self.get_passe_decisive()}
Carton Rouge : {self.get_cart_rouge()}
Carton Jaune : {self.get_cart_jaune()}""")

class Equipe:
    def __init__(self,nom_equi):
        self.__nom_equi = nom_equi
        self.__list_joueur = []
        
    def get_nom_equi(self):
        return self.__nom_equi
        
    def get_list_joueur(self):
        return self.__list_joueur
    def set_list_joueur(self,list_joueur):
        self.__list_joueur = list_joueur
        
    def ajouterJoueur(self,joueur):
        self.__list_joueur.append(joueur)

    def afficherStatistiqueJoueur(self):
        for nom in self.__list_joueur:
            nom.afficherStatistique()
            
    def mettreAJourStatistiquesJoueur(self,joueur,buts,passes,carton_jaune,carton_rouge):
        joueur.set_nb_but(buts)
        joueur.set_passe_decisive(passes)
        joueur.set_cart_jaune(carton_jaune)
        joueur.set_cart_rouge(carton_rouge)
    
joueur1 = Joueur("Lucas",1,"attaquant")
joueur2 = Joueur("Iribaren",2,"défenseur")
joueur3 = Joueur("Lucy",3,"attaquant")
joueur4 = Joueur("Vanny", 4,"défenseur")
equipe1 = Equipe("OM")
equipe2 = Equipe("PSG")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe1.ajouterJoueur(joueur3)
equipe1.ajouterJoueur(joueur4)
equipe1.afficherStatistiqueJoueur()
joueur1.effectuerUnePasseDecisive()
joueur3.marquerUnBut()
joueur4.recevoirUnCartonJaune
joueur1.marquerUnBut()
joueur4.recevoirUnCartonRouge()
joueur3.effectuerUnePasseDecisive()
joueur1.marquerUnBut()
joueur2.recevoirUnCartonJaune
joueur3.marquerUnBut()
joueur2.recevoirUnCartonRouge()
equipe1.afficherStatistiqueJoueur()
equipe1.mettreAJourStatistiquesJoueur(joueur1,4,5,0,0)

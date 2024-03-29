import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(1, 10)

        print(f"{self.nom} attaque {adversaire.nom} et lui inflige -{degats} HP.\n")
        adversaire.vie -= degats

class Jeu:
    def __init__(self):
        self.niveau = 1
        self.prenom = ""
    def choisirNiveau(self):
        self.niveau = int(input("Level (1, 2, 3) : "))
        self.prenom = (input("Player Name : "))

    def lancerJeu(self):
        self.choisirNiveau()

        hp_joueur = self.niveau * 10
        hp_ennemi = self.niveau * 10 + random.randint(1, 10)

        joueur = Personnage(self.prenom, hp_joueur)
        ennemi = Personnage("Ennemi", hp_ennemi)

        print(f"Level: {self.niveau} Fight : {joueur.nom}({joueur.vie} HP) VS {ennemi.nom} ({ennemi.vie} HP\n).\n")

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            
            if ennemi.vie <= 0:
                print(f"WIN ! Vous avez gagné contre {ennemi.nom}")
                break

            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"GAME OVER ! L'{ennemi.nom} a gagné contre {joueur.nom}")
                break

            print(f"\nPlayer : {joueur.nom} ({joueur.vie} HP) VS {ennemi.nom} ({ennemi.vie} HP).\n")

parti1 = Jeu()
parti1.lancerJeu()

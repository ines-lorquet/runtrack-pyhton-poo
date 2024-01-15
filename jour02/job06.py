class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        if self.__statut_commande == "en cours":
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "en cours"}
            print(f"Plat ajouté : {nom_plat} ({prix_plat} €)")

    def annuler_commande(self):
        if self.__statut_commande == "en cours":
            self.__plats_commandes.clear()
            self.__statut_commande = "annulée"
            print("Commande Annulé")

    def __calculer_total(self):
        total = 0
        for plat in self.__plats_commandes.values():
            total += plat["prix"]
        return total

    def afficher_commande(self):
        print(f"\nCommande #{self.__numero_commande}")
        for nom_plat, details_plat in self.__plats_commandes.items():
            print(f"{nom_plat} au prix de {details_plat['prix']} € ({details_plat['statut']})")
        total = self.__calculer_total()
        print(f"A payer : {total} € (TVA incluse)")

    def calculer_tva(self):
        total = self.__calculer_total()
        tva = total * 0.2 
        print(f"TVA : {tva} €")


commande1 = Commande(1)
commande1.ajouter_plat("Tacos double viande", 10)
commande1.ajouter_plat("Pâtes Carbonara et Caviar", 25)
commande1.afficher_commande()
commande1.calculer_tva()
commande1.annuler_commande()

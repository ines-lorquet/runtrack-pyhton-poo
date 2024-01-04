class Tache:
    def __init__(self, titre, description):
        self.__titre = titre
        self.__description = description
        self.__statut = "à faire"

    def get_titre(self):
        return self.__titre
    def set_titre(self, titre):
        self.__titre = titre

    def get_description(self):
        return self.__description
    def set_description(self, description):
        self.__description = description

    def get_statut(self):
        return self.__statut
    def set_statut(self, statut):
        self.__statut = statut


class ListeDeTaches:
    def __init__(self):
        self.lst_taches = []

    def ajouterTache(self, tache):
        self.lst_taches.append(tache)
        return f"""
La tâche {tache.get_titre()} a été ajoutée"""

    def supprimerTache(self, tache):
        self.lst_taches.remove(tache)
        return f"""
La tâche {tache.get_titre()} a été supprimée"""

    def marquerCommeFinie(self, tache):
        tache.set_statut("terminée")
        return f"La tâche {tache.get_titre()} a été marquée comme terminée"

    def afficherListe(self):
        for tache in self.lst_taches:
            print(f"Titre: {tache.get_titre()}   Description: {tache.get_description()}   Statut: {tache.get_statut()}")
            
    def filterListe(self):
        for tache in self.lst_taches:
            if tache.get_statut() == "terminée":
                return f"""
La tâche {tache.get_titre()} est {tache.get_statut()}"""


tache1 = Tache("sol", "laver le linge")
tache2 = Tache("repas", "faire le repas")
tache3 = Tache("menage", "laver le sol")
taches = ListeDeTaches()

print(taches.ajouterTache(tache1))
print(taches.ajouterTache(tache2))
print(taches.ajouterTache(tache3))
print(taches.marquerCommeFinie(tache1))
taches.afficherListe()
print(taches.supprimerTache(tache2))
print(taches.filterListe())

class Personnage:
    def __init__(self,x,y):
        self.position_x = x
        self.position_y = y
        
    def gauche(self):
        self.position_x -=1
        print("Position pour aller à gauche",self.position_x)  

    def droite(self):
        self.position_x +=1
        print("Position pour aller à droite",self.position_x) 

    def bas(self):
        self.position_y -=1
        print("Position pour aller à bas",self.position_y)
        
    def haut(self):
        self.position_y +=1
        print("Position pour aller à haut",self.position_y)  

    def position(self):
        position_tuple=(self.position_x,self.position_y)
        print(position_tuple)

afficher_position = Personnage(10,20)
afficher_position.gauche()
afficher_position.droite()
afficher_position.bas()
afficher_position.haut()
afficher_position.position()
class Point:
    def __init__(self,x,y):
        self.coor_x = x 
        self.coor_y = y 

    def afficherLesPoints(self):
        print("coordonné de x",self.coor_x,"coordonné de y",self.coor_y)

    def afficherX(self):
        print("coordonné de x",self.coor_x)

    def afficherY(self):
        print("coordonné de y", self.coor_y)
    
    def changerX(self):
        self.coor_x = 102

    def changerY(self):
        self.coor_y =300

donner= Point(100,210)
donner.afficherLesPoints()
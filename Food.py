
class Food(object) :

    def __init__(self,mydamier) : 

        self.alive = True
        self.energy = 1
        self.mydamier = Damier()

    def restore(self) : 

        self.alive = True
        self.energy = 1

    def repop(self,turn):

        if turn % 3 == 0 :
            
            self.restore()


    @abstractmethod
    def eatable(self): 
        pass

class Grass(Food): 
    super().__init__(mydamier)

    self.name = "grass"


     # qui peut en manger 
    def eatable(self):

        self.eatable = ["prey"]
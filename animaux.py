#! usr/bin/python3

import random
from Damier import Damier
from abc import ABC, abstractmethod


class Animal(ABC):

    directions = ['N','S','E','O','NE','NO','SE','SO','null']

    full = 5

    emotional_states = ["satiated","relieved","afraid","hurt","hungry"]
    
    def __init__(self,mydamier) :

        

        self.name = "animal"

        self.energy = Animal.full

        self.alive = True

        self.damier = mydamier

        self.front = random.randint(0,len(Animal.directions))

        self.memory = None

        self.emotional_state = random.randint(0,len(Animal.emotional_states))

        self.food = "food"

        self.hungry = False



    @abstractmethod

    def type_animal(self):

        pass

    def feed(self,food) : 

        if self.energy < 5 : 
            self.energy += 2
    
    # def move(self,sense) : 

    #     self.moves = sense
    #     self.front = self.moves

    def turn(self,sense) :
        
        self.turn = sense
        self.front = self.turn

    def see(self,place):

        if place : 

            self.spotted = True
        
        else : 

            self.spotted = False

    @abstractmethod
    def move(self,dirs) : 

        pass


class sheep(Animal) :

    def __init__(self,mydamier) :

        super().__init__(mydamier)

        print("bêêêêê je suis un mouton\n")

        self.food = "grass"

    def type_animal(self):

        self._type_animal = "prey"

    def hungry(self):
        
        if self.energy < 2 : 
            self.hungry = True

class wolf(Animal) :
    def __init__(self,mydamier) :

        super().__init__(mydamier)

        print("graouuuu je suis un loup\n")

        self.food = "prey"
        self.hungry = True

    def type_animal(self):

        self._type_animal = "predator"


if __name__ == '__main__':

    mouton = sheep(Damier())
    print("{}\n".format(mouton))
    loup = wolf(Damier())
    print(loup)
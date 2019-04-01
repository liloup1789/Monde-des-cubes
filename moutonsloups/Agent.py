#! usr/bin/python3
#from Table import Table
#from Recette import *
#import networkx as nw

from random import randint,shuffle
import time,sys
from pprint import pprint
# import Agent_lvl1

class Agent(object):
    
    def __init__(self,myworld,mypop):
        self.percept = {}
        self.internal = {}
        self.effect = {}
        self.world = myworld
        self.population = mypopulation
        self.id = 
        del Agent.agent_id[Agent.n_id]
        self.pos = (0,0)
        Agent.n_id += 1


    def around(self) : 
        x = 0
        y = 0
        self.percept = {self.id:[x,y]}

    def intern (self):
        self.internal = {self.id:self.pos}
    
    def active (self,position):
        # print(position)
        self.effect = {self.id:Agent.cogn(self,position)}

    def outch(self,pos,edge)  :

        if pos == 0 :

            # print("agent n°= "+str(self.id)+" says :oups can't go that way")
            return pos + randint(0,1)
        elif pos == edge :
            # print("agent n°= "+str(self.id)+" says :oups can't go that way")
            return pos + randint(-1,0)
        else :
            # print("agent n°= "+str(self.id)+" Clear !")
            return pos + randint(-1,1)
            
    def cogn (self,edges):
        x = Agent.outch(self,self.pos[0],edges[0])
        y = Agent.outch(self,self.pos[1],edges[1])
        return x,y

    def update_pos(self):
        # print("agent n°= "+str(self.id)+" is moving from position "+str(self.pos)+ " to "+str(self.effect[self.id]))
        self.pos = self.effect[self.id]
        print("agent n°= "+str(self.id)+" is at position "+ str(self.pos))

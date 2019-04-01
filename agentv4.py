#! usr/bin/python3
#from Table import Table
#from Recette import *
#import networkx as nw

from random import choice,randint,shuffle
import time,sys
import collections
from pprint import pprint
from memoryV3 import Memory
# from Oracle import Oracle
# import Agent_lvl1



class Agent(object):
    
    possible_actions = ['O','N']

    possible_internal = ["happy","unhappy"]
    
    def __init__(self,mymemory):
        
        
        self.perception = []
        self.memory = mymemory
        self.act = object
        self.satisfaction = int
        self.internal = object
        self.closest = []




    def intern (self):
        
        self.internal = {self.id:self.pos}
    

    def cogn (self):

        action,index =  self.stockInMemory(self.vector)
        if not action : 

            action = self.findSimilar(index)
        
        self.act = action
        return index

    def stockInMemory(self,current_vector):


        if not self.memory.isIdentical(current_vector) :
            print("NOT IDENTICAL\n")

            self.memory.memory[current_vector] = 1
            action = None

        else : 

            action = self.memory.getAction(current_vector)

        self.current = (current_vector,self.memory.memory[current_vector])

        pprint(self.memory.memory)
        self.memory.TreeMemory()
        self.memory.dict2list()
        index = self.memory.memory.index(self.current)

        return action,index

    def addReward(self,reward):

        if reward == 1 :
            self.satisfaction += 1
            self.internal = 'happy'
            print(" YEAH !!!!!")
        else :
            self.satisfaction -= 1
            self.internal = "unhappy"
            print(" NON C EST NUL  !!!!!")
        self.perception[2] = self.satisfaction
        self.perception[1] = self.internal

        self.updateVector()



    def updateMemory(self,index,reward) :

        self.addReward(reward)
        if index >=0 :
            print(self.memory.memory)
            print(len(self.memory.memory))
            print(index)
            print(self.memory.memory[index])
            self.memory.memory[index] = (self.vector,1)
        self.memory.Ordered2dict()


    def buildPerception(self,percept,internal,satisfaction):

        self.perception = [percept,internal,satisfaction]


    def updateVector(self):

        self.vector = (tuple(self.perception),self.act)


    def findSimilar(self,index) : 

        try : 

            similars = [ self.memory.memory[i] for i in range(index -2,index +3)]

        except IndexError : 

            similars = [i for i in self.memory.memory]

        similars.pop(similars.index(self.current))

        candidates = []

        found = False

        for similar in similars : 

            if self.memory.vectorDistance(self.current,similar) < 3:

                    candidates.append(similar)

        if not candidates : 

            candidates = similars 


        chosen_one = candidates[randint(0,len(candidates)-1)]
        print("chosen one : "+str(chosen_one))

        action = self.memory.getAction(chosen_one[0])


        #     for similar in similars : 

        #         internal = self.memory.getInternal()

        #         if internal == 'happy' : 
        #             candidates.append(similar)




        # else : 

        #     for candidate in candidates : 

        #         if internal == 'happy' : 

        #             action = self.memory.getAction(candidate)

        #             found = True 

        #             break 

        # print(len(candidates))
        # if not found : 

        #     action = possible_actions[randint(0,len(possible_actions)-1)]

        return action



     #**********************************************************
     #**********************************************************   

class Oracle(Agent):



    def __init__(self,mycorpus,mymemory):

        self.corpus = mycorpus
        self.perception = []
        self.act = object
        self.memory = mymemory
        self.satisfaction = int
        

    def awardAndPunish(self,answer) : 

        print("prediction : "+answer)
        print("expected : "+self.expected)
        if answer == self.expected :
            return 1 

        else : 
            return 0

    def buildPerfectMemory(self):


        for perception,action in self.corpus : 

            perception = (perception,0)

            self.memory.memory[(perception,action)] = 0

        

    def chooseAction(self) :

        


        # minifreq = self.memory.memory[randint(0,len(self.memory.memory)-1)][1]
        # minisat = self.memory.memory[randint(0,len(self.memory.memory)-1)][0][0][1]
        # for i in self.memory.memory :
        #     if i[1] < minifreq or i[0][0][1] < minisat:
        #         candidates.append((i,self.memory.memory.index(i)))
        #         minifreq = i[1]
        #         minisat = i[0][0][1]


        # if not candidates : 
        #     random = randint(0,len(self.memory.memory)-1)
        #     print("no candidate")
        #     candidates.append((self.memory.memory[random],random))     
        # # candidates = [i for i in self.memory.memory if [i][1] == min([j[1] for j in self.memory.memory])] # = frequency

        # # candidates = [i for i in candidates if [i][0][0][1] == min(j[0][0][1] for j in candidates)]  # = satisfaction
        

        random = randint(0,2)
        
        self.memory.TreeMemory()

        self.memory.dict2list()

        # self.current = candidates[random]

        self.current = self.memory.memory[random]
        self.perception_action = self.current[0]
        self.perception = self.perception_action[0]
        self.percept = self.perception[0]
        self.expected = self.perception_action[1]
        self.frequency = self.current[1]
        self.satisfaction = self.perception[1]
        self.current = (self.current[0],self.frequency + 1)

        print("vecteur oracle :"+str(self.current))

        return random

    def percieveAndJudge(self,percept) :

        judgment = self.awardAndPunish(percept)
        print("jugement : "+str(judgment))
        
        if judgment == 1 : 

            self.satisfaction += 1

        else : 

            self.satisfaction -= 1          

        return judgment


    def updateOracle(self,index) : 

        self.perception = (self.percept,self.satisfaction)
        self.perception_action = (self.perception,self.expected)
        self.current = (self.perception_action,self.current[1])
        print(index)
        print(self.memory.memory)
        print(len(self.memory.memory))
        self.memory.memory[index] = self.current
        self.memory.Ordered2dict()




if __name__ == '__main__':

    corpus  = [('a',"O"),('b',"N" ),('c',"N"  ),('d',"N"  ),('e',"O"),('f',"N"),('g',"N"  ),('h',"N"  ),('i',"O"),('j',"N"    ),('k',"N"  ),('l',"N"  ),('m',"N"  ),('n',"N"  ),('o',"O"),('p',"N"    ),('q',"N"  ),('r',"N"  ),('s',"N"  ),('t',"N"  ),('u',"O"),('v',"N"    ),('w',"N"  ),('x',"N"  ),('y',"O"),('z',"N"    )]
    
    oracle = Oracle(corpus,Memory())

    # print(oracle.corpus) 

    oracle.buildPerfectMemory()

    # sys.exit()

    a = Agent(Memory())
    a.internal = "happy"
    a.satisfaction = 0

    x = 0 
    while x < 4000 :
        a.closest = []
        print("\n***********************\n***********************\n\n\n"+str(x+1)+"e tour\n")
        index = oracle.chooseAction()
        numero = randint(0,25)
        #print(numero)
        percept = oracle.percept
        expected =  oracle.expected
        print("new percept : ",percept)
        print("expected answer : "+expected)
        x += 1

        if not a.memory.memory :
            action = randint(0,1)
            a.act = Agent.possible_actions[action]
            a.buildPerception(percept,a.internal,a.satisfaction)
            a.updateVector()
            print("current perception : "+str(a.perception))
            print("current vector : "+str(a.vector))
            print("chosen action : "+str(a.act))
            reward = oracle.percieveAndJudge(a.act)
            # reward = oracle.awardAndPunish(a.act,expected)
            a.addReward(reward)
            a.memory.memory[a.vector] =1
            print("current satisfaction = "+str(a.satisfaction))
            oracle.updateOracle(index)

            a.updateVector()
            print("memory is now : "+str(a.memory.memory))
            continue

        else :


            a.buildPerception(percept,a.internal,a.satisfaction)

            print("current perception : "+str(a.perception))
            a.updateVector()
            print("current vector : "+str(a.vector))
            # a.listClosest(percept,edge = 3)

            # similar,freq = a.chooseClosest()
            # same = a.stockInMemory(a.vector)
            # if same :
            #     action, index = a.findSimilar(a.vector)

            index = a.cogn()
            print("chosen action : "+str(a.act))
            reward = oracle.percieveAndJudge(a.act)
            a.updateMemory(index,reward)
            print("current satisfaction = "+str(a.satisfaction))
        
            oracle.updateOracle(index)
            # sys.exit()
            print("memory is now : "+str(a.memory.memory))
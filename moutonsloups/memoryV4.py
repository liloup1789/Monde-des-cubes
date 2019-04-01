#! usr/bin/python3


# coding: utf-8

import itertools
from scipy.spatial import distance
import numpy as np
import collections
import Levenshtein as lv
class Memory(object):

	def __init__(self):

		self.memory = {}


	def dict2list(self): 

		self.memory = list(self.memory.items())

	def vectorDistance(self,current_vector,memory_vector) :

		return lv.distance(repr(current_vector[0]),repr(memory_vector[0]))
	
	def TreeMemory(self):

		self.memory = collections.OrderedDict(sorted(self.memory.items(), key=lambda t: t[0]))

	def Ordered2dict(self) :

		self.memory = dict(self.memory)	
	
	def addReward(self,perception,reward) :

		perception.append(reward)

	def getPercept(self,perception):
		return perception[0]


	def getInternal(self,perception):
		return perception[1]


	def getSatisfaction(self,perception):
		return perception[2]


	def getAction(self,vector):

		return vector[1]

	def getFrequency(self,vector): 

		return self.memory[vector]

	def closePercept(self,new_percept):

		u = str(new_percept)
		v = str(self.getPercept())
		#print("u -  v :",str((u,v)))
		#print(lv.distance(u,v))

		return lv.distance(u,v)

	def MaxSatisfaction(self,new_satisfaction):

		u = new_satisfaction
		v = self.getSatisfaction()
		#print("max :u ,  v  = ",str((u,v)))
		#print(max(u,v))

		return max(u,v)

	def closeInternal(self,new_internal):
		
		u = str(new_internal)
		v = str(self.getInternal())
		#print("u -  v :",str((u,v)))
		#print(lv.distance(u,v))

		return lv.distance(u,v)

	def closeReward(self,new_reward):


		u = new_reward
		v = self.getReward()
		#print("u -  v :",str(abs((u - v))))
		#print(abs(u-v))

		return lv.distance(u,v)

	def closeAction(self,new_action,action):


		u = str(new_action)
		v = str(self.getAction(action))
		#print("u -  v :",str((u,v)))
		#print(lv.distance(u,v))

		return lv.distance(u,v)


	def isIdentical(self,new_vector):

		if new_vector in self.memory :

			self.memory[new_vector] += 1

			return True

		else : 
			return False


	# def treeMemory(self,new_vector,edge):

	# 	if not isIdentical(self,new_vector) :

	# 		for x in range(len(self.memory)) 

	# 			vector = self.memory[x][0]

	# 			if closePercept(self.perception,new_vector) < edge : 
	# 				#print("is close ! ")
	
	# def PutQuadru(self,distance,new_vector):

		

	# 	closest = [tuple]*10

	# 	for x in range (len(self.memory)) :

	# 		if new_vector == self.memory[x][0] :

	# 			self.memory[0][1] += 1
				

	# 		else : 
				

	# 			closest.append(quadruplet[0])




if __name__ == '__main__':
	
	memory = Memory()

	memory.buildPerception("a",'neutral',0)



	memory.buildVectorPA()

	memory.closePercept("b")

	memory.closeInternal("unhappy")

	memory.closeReward(-1)

	memory.closeAction("yes","yes")



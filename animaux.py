#! usr/bin/python3

import random

class Animaux(object):

	directions = ['N','S','E','O','NE','NO','SE','SO','null']

	full = 5

	emotional_state = ["satiated","relieved","affraid","hurt","hungry"]
	
	def __init__(self,mydamier) :

		

		self.name = "animal"

		self.energy = full

		self.alive = True

		self.damier = mydamier

		self.front = random.randint(0,len(directions))

		self.memory = None




	def feed(self,food) : 

		if self.energy < 5 : 
			energy += 1
	
	def move(self,sense) : 

		self.moves = sense
		self.front = self.moves


	def turn(self,sense) :
		
		self.turn = sense
		self.front = self.turn

	def see(self,place):

		if place : 

			self.spotted = True
		
		else : 

			self.spotted = False
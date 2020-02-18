#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
classes de base pour chatbot
il faut un monde et un agent

    l"agent il perçoit
    il agit
    il possède un état interne
    il mémorise
    il récupère l'information
    il s'évalue
    il a un but pré-câblé

    le monde a un cadre
    il envoie des perceptions
    il envoie des actions

"""


class World(object) :

    def __init__(self):

        self.members = []
        self.frame = ""
        self.turn = 0
        self.end_dialogue = False
        self.end_turn = False

    def parley(self):

        pass

    def send_perception(self):

        pass

    def send_action(self):
        pass

    def send_reward(self):
        pass

    def send_end(self):
        if self.end_dialogue :
            return True

class Agent(object) :

    goal = ""

    def __init__(self,mymemory):

        self.perception = {}
        self.action = {}
        self.internal = {}
        self.memory = mymemory


    def percieve(self):

        self.perception[1] = send_perception()


    def act(self):

        self.action = send_action()


    def update_internal(self):

       pass

    def update_satisfaction(self):

       pass
    def evaluate(self):


        if self.perception['reward'] >=1 :

            Agent.goal = True

        else :

            Agent.goal = False

    def memorize(self):

        self.memory.long_term.append(self.internal)

        last = max([k for k in self.perception if type(k) == int])

        self.memory.short_term = self.internal[-2:]

    def retrieve(self):

        if self.percept in self.memory.long_term :
            enriched_percept = max_satisfaction(self.percept)
        if self.percept in self.memory.short_term :
            enriched_percept = mesure_accuracy(enriched_percept)
        return enriched_percept


class RepeatAgent(Agent) :


    def __init__(self,world):

        Agent.__init__(self)
        self.satisfaction = 1
        self.world = world

    def percieve(self):

        self.percept = self.world.send_perception()

        enriched_percept = self.retrieve()

        if not self.perception :
            print("first perception\n")

            self.perception[1] = enriched_percept

            self.perception[1].append('first')

            self.perception[1].append(self.perception[1][0])

            self.perception['reward'] = 1
            self.update_satisfaction()
            self.internal[frozenset(self.perception)] = [self.satisfaction]
            self.internal[frozenset(self.perception)].append(1)
            print(self.internal)


        else :

            last = max([k for k in self.perception if type(k) == int ])

            self.perception[last+1] = enriched_percept

            self.perception[last+1].append(f"{last+1}st")

            self.perception[last+1].append(self.perception[last+1][0])
            self.perception['reward'] += self.world.send_reward()

            self.internal[frozenset(self.perception)] = [self.satisfaction]
            self.internal[frozenset(self.perception)].append(last+1)

    def update_internal(self):

        self.internal[frozenset(self.perception)].append(self.action)


    def act(self):

        self.action = self.world.send_action()
        print(f" action ={self.action}")
        self.update_internal()

        self.memorize()


    def update_satisfaction(self):
        n = len([k for k in self.perception]) - 1

        self.satisfaction = self.perception['reward'] / n


class OneAgentWorld(World) :
    """
    Monde qui prend un seul agent interagissant en répétant ce que lui dit le monde. Uniquement là pour implémenter des classes basiques

    """
    def __init__(self):
        World.__init__(self)

        self.members= [RepeatAgent(self)]

        self.message = ""

        self.previous_message = ""

        self.next_message = ""

    def setmessage(self,message):
        self.message = message

    def parley(self):
        self.end_turn = False
        self.members[0].percieve()

        self.members[0].act()

        self.end_turn = True

        self.turn += 1

    def send_perception(self):
        print(f'message ={self.message}')
        return self.message

    def send_action(self):
        return self.members[0].perception[self.turn+1][2]

    def send_reward(self):
        return 1


class Memory(object) :

    def __init__(self):

        self.size = 'infinite'
        self.content = []

    def access(self,elem):

        for chose in self.content :
            if elem in chose :
                return chose

    def stock(self,elem):

        if elem not in self.content :
            self.content[elem] = 1
        else :
            self.content[elem] += 1


class ShortTermMemory(Memory) :

    def __init__(self):
        Memory.__init__(self)
        self.size = 12

    def forget(self):
        if len(self.content) == self.size :
            self.content.pop(0)


class LongTermMemory(Memory) :

    def __init__(self):
        Memory.__init__(self)

    def weighting(self):

        for i in range(len(self.content)) :
            elem['weight'] = 1/(len(self.content)-i)


if __name__ == '__main__':

    list_messages = ['ga','beu','zu','mo']
    world = OneAgentWorld()
    for i  in range(len(list_messages)) :
        world.setmessage(list_messages[i])
        print(world.turn)
        try :
            world.next_message = list_messages[i+1]
        except IndexError :
            world.end_dialogue = True
        world.parley()
        print(world.members[0].internal)
        if world.end_dialogue :
            print(f'le dialogue est fini avec une satisfaction moyenne de {world.members[0].satisfaction}')
            break



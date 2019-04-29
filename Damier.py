import time,sys
from pprint import pprint




class Damier(object) :

    def __init__(self):
        self.length = 10
        self.height = 10
        self.damier = []
        if length == height : 
            self.type = "square"
        else : 
            self.type = "rectangle"

        for x in range(length):
            self.damier.append([])
            for y in range(height):
                self.damier[x].append(0)
        self.edges = (length,height)

    def update_world(self,old,new,turn,objet):
        self.damier[new[0]][new[1]] = objet
        if turn != 0: 
            self.damier[old[0]][old[1]] = 0
            
    
#     def afficher(self,lignes = "") :
#             lignes = [[] for i in range(self.length)]
#             damier = "" # print(self.damier)
#             for x_range in self.damier: 
#                 # print(x_range)
#                 ligne  = ""
#                 x = 0
#                 for i in range (self.height-1,-1,-1):
#                     #print(i)





#                     # print (x_range[i])
#                     lignes[x].append(x_range[i])
#                     x += 
#                 #     ligne  = str(x_range[i])+'-'+ligne
#                 # #for case in ligne: 
#                 #     #colonne += case +'-'
#                 # print(ligne[:-1])
#                 # lignes = ligne[:-1]+'\n'+lignes
#             print('\n\n\n')
#             # print(lignes)
#             for ligne in lignes : 
#                 str_line = ""
#                 for elem in ligne : 
#                     str_line += str(elem)+'-'
#                 str_line = str_line[:-1]+'\n'
#                 damier += str_line
#             print(damier)

#     def run (self,nr_agents,turns):
#         agents = []
#         turn = 0
#         for x in range(1,nr_agents+1):
#             agents.append(Agent_lvl1())
#         while turn < turns : 
#             print("turn number "+str(turn)+"\n\n")
#             for agent in agents :
#                 pos = agent.pos
#                 agent.active(self.edges)
#                 Damier.update_world(self,pos,agent.effect[agent.id],turn)
#                 agent.update_pos()
#                 agent.update_view()
#                 # agent.update_direction(self.edges)
#                 pprint(agent.direction)
#             time.sleep(1)    
#             Damier.afficher(self)
            
#             # sys.exit()
#             turn += 1

#     def main():
#         d = Damier(10,10)
#         d.run(1,10)

# if __name__ == '__main__':
#     Damier.main()
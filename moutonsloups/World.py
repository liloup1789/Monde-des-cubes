#! usr/bin/python3
#from Table import Table
#from Recette import *
#import networkx as nw

from random import randint,shuffle
import time,sys
from pprint import pprint

from namelistmap import namelistmap

class World( object ):
    
    def __init__( self, maxpop, lifelength, width, height ):
        #---- la population ---
        self.first_agent_id = 0
        self.max_population = maxpop
        self.population = namelistmap()  # key = agent_id and value = agent.self
        self.n_id = self.first_agent_id 
        #----- le temps ---
        self.agent_lifetime = lifelength
        self.max_time = self.agent_lifetime * self.max_population   # je ne comprends pas cette ligne 
        self.time = 0
        #---- l'espace ---
        self.orientations = [ 'north', 'south', 'east', 'west' ]
        self.max_x = width
        self.max_y = height
        self.space = namelistmap()  # key = (x,y) and value = agent_id
        self.physical_space = []

        for x in range( self.max_x ):
            self.physical_space.append([])
            for y in range( self.max_y ):
                self.physical_space[ x ].append( 0 )
        #--- population creation ---
        for i in range( self.first_agent_id, self.max_population ):
            self.new_agent = Agent( self )
            self.population.add( self.new_agent.id, self.new_agent )
            assert( self.population.get( i )[0] == self.new_agent )
            self.space.add( self.new_agent.pos, self.new_agent )
            print( 'added agent {0} of type {1} with id {2}'.format( self.new_agent, type( self.new_agent ) , self.new_agent.id ))
        self.afficher()
        #---- et le monde tourne ---
        self.run()  

    def new_id( self ):
        if( self.n_id < self.max_population ):
            self.curr_id = self.n_id
            self.n_id += 1
            assert( self.population.get( self.curr_id ) is None ) 
            return( self.curr_id  )
        else:
            print( 'ERROR cannot create the new agent id {0}\n it exceeds the max population size {1}'.format( self.n_id, self.max_population))
            assert( False )

    def new_location( self ):
         if( self.space_full() ):
              print( 'ERROR cannot assign a free location, all available space is used by the population (two agents cannot occupy the same location)')
              assert( False )
         else:
             new_pos = (randint( 0, (self.max_x - 1)), randint( 0, (self.max_y -1) ) )
             while( new_pos in self.space.get_all_keys() ):
                 new_pos = (randint( 0, (self.max_x - 1)), randint( 0, (self.max_y -1) ) )
             return( new_pos )
         
    def space_full( self ):
        return( (len( self.space.get_all_keys()) == (self.max_x * self.max_y)) and (len( self.space.get_all_keys()) <= len( self.population.get_all_keys())) )

    def run( self ):
         while( self.time < self.max_time ):
            for id in self.population.get_all_keys():
                self.population.get( id )[0].activate()
            self.afficher()
            print( 'time is {0}'.format( self.time ) )
            self.time += 1

    def afficher(self,lignes = "") :
        print()
        line = '    '
        for x in range( 0, self.max_x ):
            line += '='
        print( line )
        for y in reversed( range( 0, self.max_y ) ):
            line = '{0}  |'.format( y )
            for x in range( 0, self.max_x ):
                agent_lst = self.space.get( (x, y) )
                if( (agent_lst is not None) and (agent_lst != [] )):
                    line += str( agent_lst[ 0 ].id )
                else:
                    line += '.'
            line += '|'
            print( line )
        line = '    '
        for x in range( 0, self.max_x ):
            line += '='
        print( line )
        line = 'y/x '
        for x in range( 0, self.max_x ):
            line += '{0}'.format( x )
        print( line )
        print()
        print()

    def is_free( self, pos ):
        return( self.space.get( pos ) is None )

    def inside_space( self, pos ):
        return( (pos[0] >= 0) and (pos[1] >= 0) and (pos[ 0 ] < self.max_x) and (pos[ 1 ] < self.max_y))

    #----------- agents management
        
    def agent_try( self, agent ):
        self.target_pos = (0,0)
        if( agent.action_try != 'nop' ):    
            if( agent.action_try == 'move_right' ):
                if( agent.orientation == 'north' ): self.target_pos = ((agent.pos[ 0 ]+1), agent.pos[ 1 ])
                if( agent.orientation == 'south' ): self.target_pos = ((agent.pos[ 0 ]-1), agent.pos[ 1 ])
                if( agent.orientation == 'east' ):  self.target_pos = (agent.pos[ 0 ], (agent.pos[ 1 ]-1))
                if( agent.orientation == 'west' ):  self.target_pos = (agent.pos[ 0 ], (agent.pos[ 1 ]+1))
            if( agent.action_try == 'move_left' ):
                if( agent.orientation == 'north' ): self.target_pos = ((agent.pos[ 0 ]-1), agent.pos[ 1 ])
                if( agent.orientation == 'south' ): self.target_pos = ((agent.pos[ 0 ]+1), agent.pos[ 1 ])
                if( agent.orientation == 'east' ):  self.target_pos = (agent.pos[ 0 ], (agent.pos[ 1 ]+1))
                if( agent.orientation == 'west' ):  self.target_pos = (agent.pos[ 0 ], (agent.pos[ 1 ]-1)) 
            if( agent.action_try == 'move_forward' ):
                if( agent.orientation == 'north' ): self.target_pos = (agent.pos[ 0 ], (agent.pos[ 1 ]+1))
                if( agent.orientation == 'south' ): self.target_pos = (agent.pos[ 0 ], (agent.pos[ 1 ]-1))
                if( agent.orientation == 'east' ):  self.target_pos = ((agent.pos[ 0 ]+1), agent.pos[ 1 ])
                if( agent.orientation == 'west' ):  self.target_pos = ((agent.pos[ 0 ]-1), agent.pos[ 1 ]) 
            if( agent.action_try == 'move_backward' ):        
                if( agent.orientation == 'north' ): self.target_pos = (agent.pos[ 0 ], (agent.pos[ 1 ]-1))
                if( agent.orientation == 'south' ): self.target_pos = (agent.pos[ 0 ], (agent.pos[ 1 ]+1))
                if( agent.orientation == 'east' ):  self.target_pos = ((agent.pos[ 0 ]-1), agent.pos[ 1 ])
                if( agent.orientation == 'west' ):  self.target_pos = ((agent.pos[ 0 ]+1), agent.pos[ 1 ])
            if( self.inside_space( self.target_pos )):
                if( self.is_free( self.target_pos )):
                    self.change_pos( agent, self.target_pos )
                else:
                    self.hurt( agent )
            else:
                self.hurt( agent )
                
    def change_pos( self, agent, newpos ):
        self.space.remove( nm = agent.pos )
        self.space.add( newpos, agent )
        agent.moved_to( newpos )

    def hurt( self, agent ):
        agent.hurt()

    def perceive( self, agent ):
        self.agent_pos = self.space.get_key_for( agent )
        assert( type( self.agent_pos ) is tuple )
        self.neighborhood = { 'forward':None, 'backward':None, 'right':None, 'left':None }
        if( self.inside_space( ((self.agent_pos[ 0 ] - 1), self.agent_pos[ 1 ]) )):
            self.neighbor = self.space.get( ((self.agent_pos[0] -1), self.agent_pos[1] ))
        else:
            self.neighbor = 'WALL'
        if( self.neighbor is not None ):
            if( agent.orientation == 'north' ):
                self.neighborhood[ 'left' ] = self.neighbor
            if( agent.orientation == 'south' ):
                self.neighborhood[ 'right' ] = self.neighbor
            if( agent.orientation == 'east' ):
                self.neighborhood[ 'backward' ] = self.neighbor
            if( agent.orientation == 'west' ):    
                self.neighborhood[ 'forward' ] = self.neighbor
        if( self.inside_space( ((self.agent_pos[ 0 ] + 1), self.agent_pos[ 1 ]) )):
            self.neighbor = self.space.get( ((self.agent_pos[0] +1), self.agent_pos[1] ))
        else:
             self.neighbor = 'WALL'
        if( self.neighbor is not None ):
            if( agent.orientation == 'north' ):
                self.neighborhood[ 'right' ] = self.neighbor
            if( agent.orientation == 'south' ):
                self.neighborhood[ 'left' ] = self.neighbor
            if( agent.orientation == 'east' ):
                self.neighborhood[ 'forward' ] = self.neighbor
            if( agent.orientation == 'west' ):    
                self.neighborhood[ 'backward' ] = self.neighbor
                self.neighborhood
        if( self.inside_space( (self.agent_pos[ 0 ], (self.agent_pos[ 1 ] -1)) )):
            self.neighbor = self.space.get( (self.agent_pos[0], (self.agent_pos[1] -1)))
        else:
            self.neighbor = 'WALL'
        if( self.neighbor is not None ):
            if( agent.orientation == 'north' ):
                self.neighborhood[ 'backward' ] = self.neighbor
            if( agent.orientation == 'south' ):
                self.neighborhood[ 'forward' ] = self.neighbor
            if( agent.orientation == 'east' ):
                self.neighborhood[ 'right' ] = self.neighbor
            if( agent.orientation == 'west' ):    
                self.neighborhood[ 'left' ] = self.neighbor
        if( self.inside_space( (self.agent_pos[ 0 ], (self.agent_pos[ 1 ] +1)) )):
            self.neighbor = self.space.get( (self.agent_pos[0], (self.agent_pos[1] +1)))
        else:
            self.neighbor = 'WALL'
        if( self.neighbor is not None ):
            if( agent.orientation == 'north' ):
                self.neighborhood[ 'forward' ] = self.neighbor
            if( agent.orientation == 'south' ):
                self.neighborhood[ 'backward' ] = self.neighbor
            if( agent.orientation == 'east' ):
                self.neighborhood[ 'left' ] = self.neighbor
            if( agent.orientation == 'west' ):    
                self.neighborhood[ 'right' ] = self.neighbor
        return( self.neighborhood )

#----- end of class World -----
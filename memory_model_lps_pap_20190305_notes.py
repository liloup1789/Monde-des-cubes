
# la perception est une fonction des sensations et d'un certain nombres d'aller-retours entre les capteurs (qui produisent les sentations
# et les fonctions cognitives qui prennent en compte le contenu de la mémoire de travail

def cognitive_functions( ):
     return( 'cognitive function' )


class perception( object ):
    def __init__( self, init_sensation, cogfun, working_memory, sensors ):
        self.curr_percept_content = None  # au réveil de l'agent
        self.saliency = None
        return( self.build_perception( init_sensation, cogfun, working_memory, sensors ))
        
    def build_perception( self, sensation, cogfun, working_memory, sensors ):
        if( not self.percept_stabilized_p( self.curr_percept ) ):
            # influence de l'état des capteurs et des fonctions cognitives sur les sentations lors de leur mise à jour
            updated_sensation = cogfun( sensors( sentation))
            self.saliency = self.update_saliency( updated_sensation, working_memory )
            # influence de la mémoire de travail sur la perception (modification de la saillance)
            self.curr_percept_content, self.saliency = self.build_perception( updated_sensation,
                                                                              cogfun,
                                                                              working_memory,
                                                                              sensors )
    def percept_stabilized_p( object ): # TODO 
        # critère d'arrêt booléen
        return( (self.curr_percept_content is not None) and (self.saliency is not None)) # pour le momen on fait simple


class working_memory(): # TODO
    def __init__( self ):
        print( 'working memory' )
        # son contenu sera un graph d'items

class sensory_memory(object) :
    """
    Principe de la mémoire sensorielle ou 
    """
        def __init__( self ):
            print(' first memory of all ')



class non_declarative_memory( object ): # TODO
    def __init__( self ):
        print( 'non declarative memory' )
    # 2 aspects de cette mémoire : (à verifier si cette interprétation est correcte par rapport à la littérature!) TODO
    #   - rappel (recall) = capacité à restituer un item complet
    #   - retention = nombre maximal d'items mémorisés (trouver l'équivalent anglais) TODO
    # altération = fonction d'interférence de ce conenu avec les mémoire à long terme déclaratives et avec la perception (en particulier sa saillance)


class episodic_memory( object ): # TODO
    # memoire des événements individuels spécifics à l'agent
    def __init__( self ):
        # TO BE DEFINED la representation de l'agent lui-même:
        # self.the_agent_self
        # qui va permettre avec le contenu de la mémoire épisodic et sémantique de construire
        # les affordances
        print( 'episodic memory' )
        
    def build_affordances( self, semantic_memory ):
        print( 'build the list of affordances' )

class semantic_memory( object ): # TODO
    # mémoire des schémas récurrents moyenné des items de la mémoire épisodique
    def __init__( self, episodic_memory ):
        print( 'semantic memory' )
    

class declarative_memory( object ):  # TODO
    def __init__( self ):
        self.episo_mem= episodic_memory()
        self.semant_mem= semantic_memory()

class long_term_memory( object ):  # TODO
     def __init__( self ):
         # c'est plus souple pour les évolution futures d'avoir des data member que de procéder par héritage de long_term_memory pour
         # la mémoire procédurale et la mémoire déclarative
         self.procedural_mem = non_declarative_memory()
         self.decla_mem = declarative_memory()

# TODO
# il faut coder la boucle d'interaction de l'agent qui recoit une sentation, construit une nouvelle perception (cf ci-dessus)
# puis calcule les affordances à partir de la perception courrante, du contenu de la mémoire de travail et de la mémoire à
# long terme,
# l'ultime étape étant le choix par les fonctions cognitives de l'affordance qui sera exécutée.

class affordance( object ):   # TODO
    def __init__( self ):
        print( 'affordance' )

    

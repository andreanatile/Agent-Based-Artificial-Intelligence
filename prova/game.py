import random
import numpy as np

class Game:
    def __init__(self,intial_state,player):
        self.initial_state=intial_state
        self.player=player
        
    def action(self,state):
        return []
    
    def reuslt(self,state,aciton):
        return None
    
    def successors(self,state):
        return [(self.reuslt(state,a),a) for a in self.action(state)]
    
    def terminal_test(self,state):
        return False
    
    def utility(self,state):
        return 0
    
    def player_utility(self,state):
        if self.player=='MAX':
            return self.utility(state)
        if self.player=='MIN':
            return -self.utility(state)
        
        raise ValueError('Illegal player')
    

class Pacman(Game):
    def __init__(self,intial_state,player,size_board):
        super(Game).__init__(intial_state,player)
        self.size_board=size_board
        cells=[(row,column) for row in range(self.size_board) 
               for column in range(self.size_board)]
        self.special_cells=self.__init__special_cells()
        self.visited_state=[intial_state]
         
        
   
    def __init__special_cells(self):
        cells=[(row,column) for row in range(self.size_board) 
               for column in range(self.size_board)]
        return random.choices(cells,k=((self.size_board^2)/4))
    
    def actions(self,state):
        
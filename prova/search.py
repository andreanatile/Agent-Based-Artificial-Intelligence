import numpy as np
import random

class MiniMax:
    def __init__(self,game):
        self.game=game
        
        
    def next_move(self,state):
        if self.game.terminal_test(state):
            return self.game.utility_pplayer(state)
        
        return max(self.game.actions(state), key=lambda a:self.min_value(self.game.result(state,a)))
    
    def min_value(self,state):
        if self.game.terminal_test(state):
            return self.game.utility_player(state)
        
        return min(self.max_value(s) for s,a in self.game.successors(state))
    
    def max_value(self,state):
        if self.game.terminal_test(state):
            return self.game.utility_player(state)
        
        return max(self.min_value(s) for s,a in self.game.successors(state))
    
    
class AlphaBeta:
    def __init__(self,game):
        self.game=game
        
    def next_move(self,state):
        alpha=-np.inf()
        beta=np.inf()
        
        for s,a in self.game.successors(state):
            v=self.min_value(s,alpha,beta)
            if v> alpha:
                alpha=v
                best_move=a
                
        return best_move
    
    def max_value(self,state,alpha,beta):
        if self.game.terminal_test(state):
            return self.game.utility_player(state)
        
        v=-np.inf()
        for s,a in self.game.successors(state):
            v=max(v,self.min_value(s,alpha,beta))
            if v>=beta:
                return v
            
            alpha=max(v,alpha)
            
        return v
    
    def min_value(self,state,alpha,beta):
        if self.game.terminal_test(state):
            return self.game.utility_player(state)
        
        v=+np.inf()
        for s,a in self.game.successors(state):
            v=min(v,self.min_value(s,alpha,beta))
            if v<=alpha:
                return v
            
            beta=min(v,beta)
            
        return v
    
    

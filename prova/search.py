import numpy as np

class MinMax:
    def __init__(self,game):
        self.game=game
        
    def MinMax(self,state):
        return max(self.game.action(state), key=lambda a:
            self.min_value(self.game.result(state,a)))
        
    def min_value(self,state):
        if self.game.terminal_test(state):
            return self.game.player_utility(state)
        
        vs=[self.max_values(s) for s,a in self.game.successors(state)]
        return min(vs)
    
    def max_value(self,state):
        if self.game.terminal_test(state):
            return self.game.player_utility(state)
        
        vs=[self.min_value(s) for s,a in self.game.successors(state)]
        return max(vs)
    
    
class AlphaBeta:
    def __init__(self,game):
        self.game=game
        
    def alphabeta(self,state):
        alpha=np.inf()
        beta=-np.inf()
        return max(self.game.action(state),key=lambda a:
            self.min_value(self.game.result(state,a),alpha,beta))
        
    def max_value(self,state,alpha,beta):
        if self.game.terminal_test(state):
            return self.game.utility_player(state)
        
        v=-np.inf()
        
        for s,a in self.successors(state):
            v=max(v,self.min_value(s,alpha,beta))
            
            if v>=beta:
                return v
            
            alpha=max(v,alpha)
            
        return v
    
    def min_value(self,state,alpha,beta):
        if self.game.terminal_test(state):
            return self.game.utility_player(state)
        
        v=np.inf()
        
        for s,a in self.game.successors(state):
            v=min(v,self.max_value(s,alpha,beta))
            
            if v<=alpha:
                return v
            
            beta=min(v,beta)
            
        return v
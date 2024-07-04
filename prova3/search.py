import numpy as np


class MinMax:
    def __init__(self, game):
        self.game = game

    def next_move(self, state):
        return max(self.game.actions(state), key=lambda move: self.min_value(self.result(state, move)))

    def min_value(self, state):
        if self.game.terminal_test(state):
            return self.game.utility_player(state)

        return min([self.max_value(s) for s, a in self.game.successors(state)])

    def max_value(self, state):
        if self.game.terminal_test(state):
            return self.game.utility_player(state)

        return max([self.min_value(s) for s, a in self.game.successors(state)])


class AlphaBeta:
    def __init__(self, game):
        self.game = game

    def next_move(self, state):
        alpha = -np.inf()
        beta = np.inf()

        best_move = None
        for s, a in self.game.successors(state, alpha, beta):
            v = self.min_value(s)
            if v > alpha:
                alpha = v
                best_move = a

        return best_move

    def max_value(self, state, alpha, beta):
        if self.game.terminal_test(state):
            return self.game.utility_player(state)

        v = -np.inf()

        for s, a in self.game.successors(state):
            v = max(v, self.min_value(s, alpha, beta))
            if v > beta:
                return v

            alpha = max(v, alpha)

        return v

    def min_value(self, state, alpha, beta):
        if self.game.terminal_test(state):
            return self.game.utility_player(state)

        v = +np.inf()

        for s, a in self.game.successors(state):
            v = min(v, self.max_value(s, alpha, beta))
            if v < alpha:
                return v

            beta = min(v, beta)

        return v


class LimitedMinMax:
    def __init__(self, game, limit):
        self.game = game
        self.limit = limit

    def next_move(self, state):
        return max(self.game.actions(state), key=lambda move:
                   self.min_value(self.game.result(state, move), self.limit))
    
   
    def min_value(self, state,limit):
        if self.game.terminal_test(state) or limit==0:
            return self.game.utility_player(state)

        return min([self.max_value(s,limit-1) for s, a in self.game.successors(state)])

    def max_value(self, state,limit):
        if self.game.terminal_test(state) or limit==0:
            return self.game.utility_player(state)

        return max([self.min_value(s,limit-1) for s, a in self.game.successors(state)])


class AlphaBetaLimited:
    def __init__(self,game,limit):
        self.game=game
        self.limit=limit
        
    def next_move(self,state):
        alpha=-np.inf()
        beta=np.inf()
        
        best_move=None
        
        for s,a in self.game.successors(state):
            v=max(self.min_value(s,a,alpha,beta,self.limit))

            if v>alpha:
                best_move=a
                alpha=v
        return best_move
    
    def max_value(self, state, alpha, beta,limit):
        if self.game.terminal_test(state) or limit==0:
            return self.game.utility_player(state)

        v = -np.inf()

        for s, a in self.game.successors(state):
            v = max(v, self.min_value(s, alpha, beta,limit-1))
            if v > beta:
                return v

            alpha = max(v, alpha)

        return v

    def min_value(self, state, alpha, beta,limit):
        if self.game.terminal_test(state) or limit==0:
            return self.game.utility_player(state)

        v = +np.inf()

        for s, a in self.game.successors(state):
            v = min(v, self.max_value(s, alpha, beta,limit-1))
            if v < alpha:
                return v

            beta = min(v, beta)

        return v

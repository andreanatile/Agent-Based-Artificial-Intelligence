import numpy as np
import random


class PacManGame:
    def __init__(self, size_board, player='MAX'):
        self.size_board = size_board
        self.player = player
        self.initial_state = self.init__initial_state()

    def init__initial_state(self):
        cell = [(_, __) for _ in range(self.size_board)
                for __ in range(self.size_board)]
        k = round((self.size_board**2)/4)
        special = random.choices(cell, k=k)
        return {
            'min_pos': (self.size_board-1, self.size_board-1),
            'max_pos': (0, 0),
            'special': special,
            'to_move': 'MAX'
        }

    def actions(self, state):
        actions = ['Up', 'Down', 'Right', 'Left']

        if state['to_move'] == 'MAX':
            pos = state['max_pos']
        elif state['to_move'] == 'MIN':
            pos = state['min_pos']
        else:
            raise ValueError()

        if pos[0] == 0:
            actions.remove('Up')

        if pos[0] == (self.size_board-1):
            actions.remove('Down')

        if pos[1] == 0:
            actions.remove('Left')

        if pos[1] == (self.size_board-1):
            actions.remove('Right')

        return actions

    def result(self, state, action):
        if state['to_move'] == 'MAX':
            new_max_pos = self.computed_result(state['max_pos'], action)
            special = [special for special in state['special']
                       if special != new_max_pos]
            return {
                'min_pos': state['min_pos'],
                'max_pos': new_max_pos,
                'special': special,
                'to_move': 'MIN'
            }

        if state['to_move'] == 'MIN':
            new_min_pos = self.computed_result(state['min_pos'], action)
            new_state = dict(state)
            new_state['min_pos'] = new_min_pos
            new_state['to_move'] = 'MAX'
            return new_state

        raise ValueError()

    def computed_result(self, cell, action):
        if action == 'Up':
            return (cell[0]-1, cell[1])

        if action == 'Down':
            return (cell[0]+1, cell[1])

        if action == 'Left':
            return (cell[0], cell[1]-1)

        if action == 'Right':
            return (cell[0], cell[1]+1)

        raise ValueError()

    def utility(self, state):
        manatthan = (abs(state['max_pos'][0]-state['min_pos'][0]) +
                     abs(state['max_pos'][1]-state['min_pos'][1]))

        special = round((self.size_board**2)/4)-len(state['special'])
        return special + manatthan

    def player_utility(self, state):
        if self.player == 'MAX':
            return self.utility(state)
        if self.player == 'MIN':
            return -self.utility(state)
        
    def next_player(self):
        if self.player=='MAX':
            return 'MIN'
        if self.player=='MIN':
            return 'MAX'
        
    def temr
    def play(self,frist_player,second_player):
        players=[frist_player,second_player]
        moves=[]
        state=self.initial_states
        
        while True:
            for player in player:
                if self.
        

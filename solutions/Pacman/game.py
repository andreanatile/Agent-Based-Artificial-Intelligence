import random
import copy


class Game:
    def __init__(self, initial_state, player='MAX'):
        self.initial_state = initial_state
        self.player = player

    def actions(self, state):
        return None

    def result(self, state, action):
        return None

    def successors(self, state):
        return [(self.result(state, a), a) for a in self.actions(state)]

    def utility(self, state):
        return 0

    def player_utility(self, state):
        if self.player == 'MAX':
            return self.utility(state)

        if self.player == 'MIN':
            return -self.utility(state)
        raise ValueError()

    def terminal_test(self, state):
        return False

    def next_player(self):
        if self.player == 'MAX':
            return 'MIN'
        if self.player == 'MIN':
            return 'MAX'

        raise ValueError()

    def play(self, player1, player2):

        players = [player1, player2]
        state = self.initial_state
        moves = []
        state=self.initial_state

        while True:
            for player in players:
                if self.terminal_test(state):
                    print('Game Over')
                    return state

                move = player.next_move(state)
                state = self.result(state, move)
                self.display(state)
                moves.append(move)
                self.player=self.next_player()
        
    
    def display(self,state):
        return False


class PacMan(Game):
    def __init__(self, board_size):
        self.board_size = board_size
        initial_state = self.init_initial_state()
        super(PacMan,self).__init__(initial_state,player='MAX')
        self.min = 'MIN'
        self.max = 'MAX'
        self.empty = '.'
        self.special = '*'
        self.met = 'X'

    def init_initial_state(self):
        cells = [(_, __) for _ in range(self.board_size) for __ in range(self.board_size)
                 if (_, __) != (0, 0) and (_, __) != (self.board_size-1, self.board_size-1)]

        k = round((self.board_size*self.board_size)/4)
        special_cells = random.choices(population=cells, k=k)

        return {
            'max_cell': (0, 0),
            'min_cell': (self.board_size-1, self.board_size-1),
            'specials': special_cells,
            'to_move': 'MAX'
        }

    def actions(self, state):
        actions = ['left', 'right', 'up', 'down']

        if state['to_move'] == 'MAX':
            cell = state['max_cell']
        elif state['to_move'] == 'MIN':
            cell = state['min_cell']
        else:
            raise ValueError()

        if cell[1] == 0:
            actions.remove('left')

        if cell[1] == (self.board_size-1):
            actions.remove('right')

        if cell[0] == 0:
            actions.remove('up')

        if cell[0] == (self.board_size-1):
            actions.remove('down')

        return actions

    def result(self, state, action):

        if state['to_move'] == 'MAX':
            cell = state['max_cell']
        elif state['to_move'] == 'MIN':
            cell = state['min_cell']
        else:
            raise ValueError()

        if action == 'left':
            new_cell = (cell[0], cell[1]-1)

        if action == 'right':
            new_cell = (cell[0], cell[1]+1)

        if action == 'up':
            new_cell = (cell[0]-1, cell[1])

        if action == 'down':
            new_cell = (cell[0]+1, cell[1])

        if state['to_move'] == 'MAX':
            return {
                'max_cell': new_cell,
                'min_cell': state['min_cell'],
                'specials': [s for s in state['specials'] if s != new_cell],
                'to_move': 'MIN'
            }

        if state['to_move'] == 'MIN':
            new_state = copy.deepcopy(state)
            new_state['min_cell'] = new_cell
            new_state['to_move'] = 'MAX'
            return new_state

    def terminal_test(self, state):
        if state['max_cell'] == state['min_cell'] or state['specials'] == []:
            return True

        return False

    def utility(self, state):
        manhattan = abs(state['max_cell'][0]-state['min_cell'][0]) + \
            abs(state['max_cell'][1]-state['min_cell'][1])
        coin = round((self.board_size*self.board_size)/4)-len(state['specials'])
        return coin + manhattan
    
    
    def play(self, player_one, player_two):
        """
        A function that simulates the game between two players
        @param player_one: function that models the first player
        @param player_two:  function that models the second player
        """
        state = self.initial_state
        print("----- THE GAME STARTS! -----\n\n")
        self.draw_board(self.initial_state)
        players = [player_one, player_two]
        moves = []
        while True:
            for player in players:
                if self.terminal_test(state):
                    print('----- GAME OVER -----\n\n')
                    return moves
                else:
                    print(f'{self.player} plays!')
                move = player.next_move(state)
                state = self.result(state, move)
                self.draw_board(state)
                moves.append((move, self.player))
                self.player = self.next_player()
                print('_____________________')

    def display(self, state):
        print('_____________________')
        if self.player == 'MAX':
            print(self.player, 'in ', state['max_pos'], self.player_utility(state))
        elif self.player == 'MIN':
            print(self.player, 'in ', state['min_pos'], self.player_utility(state))
        else:
            raise ValueError

    def display_move(self, state, move):
        print(self.player, f'--{move}--> ', state)

    def draw_board(self, state):
        # print header
        print('\t', end='')
        for column in range(0, self.board_size):
            print(column, '\t\t', end='')
        print()

        for i in range(0, self.board_size):
            print(i, end='')
            for j in range(0, self.board_size):
                if (i, j) == state['min_cell'] == state['max_cell']:
                    print('\t{}\t|'.format(self.met), end=" ")
                elif (i, j) == state['min_cell']:
                    print('\t{}\t|'.format(self.min), end=" ")
                elif (i, j) == state['max_cell']:
                    print('\t{}\t|'.format(self.max), end=" ")
                elif (i, j) in state['specials']:
                    print('\t{}\t|'.format(self.special), end=" ")

                else:
                    print('\t{}\t|'.format(self.empty), end=" ")
            print()
        print()
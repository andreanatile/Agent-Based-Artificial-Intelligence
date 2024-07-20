class Game:
    def __init__(self,initial_state,player='MAX'):
        self.initial_state=initial_state
        self.player=player
        
        
    def actions(self,state):
        return None
    
    def result(self,state,action):
        return None
    
    def successors(self,state):
        return [(self.result(state,a),a) for a in self.actions(state)]
    
    def terminal_test(sef,state):
        return False
    
    def cost(self,state,action):
        return 1
    
    def utility(self,state):
        return 0
    
    def player_utility(self,state):
        if self.player=='MAX':
            return self.utility(state)
        if self.player=='MIN':
            return -self.utility(state)
        
        raise ValueError()
    
    def next_player(self):
        if self.player=='MAX':
            self.player=='MIN'
        if self.player=='MIN':
            self.player='MAX'
            

class TicTacToe(Game):
    def __init__(self,player='MAX'):
        initial_state={
            'max_cells':[],
            'min_cells':[],
            'to_move':player
        }
        
        super().__init__(initial_state,player=player)
        
        self.empty = '.'
        self.X = 'X'
        self.O = 'O'

    def actions(self,state):
        
        void_cells=[(_,__) for _ in range(3) for __ in range(3)
                        if (_,__) not in state['max_cells'] and 
                        (_,__) not in state['min_cells']]
        
        return void_cells
    
    def result(self,state,action):
        if (action in state['max_cells'] or
                action  in state['min_cells']):
            raise ValueError()
            
        if state['to_move']=='MAX':
            new_state=state.copy()
            new_state['max_cells'].append(action)
            new_state['to_move']='MIN'
            return new_state
        
        if state['to_move'] == 'MIN':
            new_state = state.copy()
            new_state['min_cells'].append(action)
            new_state['to_move'] = 'MAX'
            return new_state
        
        raise ValueError()
    
    def terminal_test(self, state):
        if self.utility(state) !=0 or (len(state['max_cells'])+len(state['min_cells']))==9:
            return True
        return False
                
    def utility(self, state):
        
        if self.player=='MAX':
            cells=state['max_cells']
        
        if self.player=='MIN':
            cells=state['min_cells']
            
        
        for i in range(3):
            # Vertical cells
            if len([cell for cell in cells if cell[1]==i])==3:
                return 1
            
            # horizontal cells
            if len([cell for cell in cells if cell[0]==i])==3:
                return 1
            
        # First diagonal
        if len([cell for cell in cells if abs(cell[0]-cell[1])==0])==3:
            return 1
        
        # Second diagonal
        if len([cell for cell in cells if abs(cell[0]+cell[1])==2])==3:
            return 1
        
        return 0
        
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
                    if self.utility(state) == 0:
                        print("IT'S A DRAW! \n\n")
                    elif self.player_utility(state) == 1:
                        print("MAX WINS! \n\n")
                    elif self.player_utility(state) == -1:
                        print("MIN WINS! \n\n")
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

    def draw_board(self, state):
        # print header
        print('\t', end='')
        for column in range(3):
            print(column, '\t\t', end='')
        print()
        copy_state = {}
        for k, v in state.items():
            if k != 'to_move':
                copy_state[k] = state[k].copy()

        for i in range(0,3):
            print(i, end='')
            for j in range(0, 3):
                if (i, j) in state['max_cells']:
                    print('\t{}\t|'.format(self.X), end=" ")
                elif (i, j) in state['min_cells']:
                    print('\t{}\t|'.format(self.O), end=" ")
                else:
                    print('\t{}\t|'.format(self.empty), end=" ")
            print()
        print()

        
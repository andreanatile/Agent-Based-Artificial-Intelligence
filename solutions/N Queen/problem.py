import random
class QueenEnvironment:
    def __init__(self,height,n_queens):
        self.height=height
        self.n_queens=n_queens

class N_QueenProblem:
    def __init__(self,environment):
        self.environment=environment
        self.initial_state = self.random()
        self.max_conflicts=sum([i for i in range(1,self.environment.n_queens)])
        
        
    def action(self,state):
        actions=[]
        for queen in range(len(state)):
            rem_position=[position for position in 
                          range(self.environment.height) if position!=state[queen]]
            
            for possible_position in rem_position:
                actions.append((queen,possible_position))
                
                
        return actions
    
    def conflits(self,state):
        conflicts=0
        for col in range(0,self.environment.n_queens):
            for col1 in range(col+1,self.environment.n_queens):
                if state[col]==state[col1]:
                    conflicts +=1
                    
                if abs(state[col]-col)==abs(state[col1]-col1):
                    conflicts +=1
                    
                if abs(col+state[col])==abs(col1+state[col1]) and col>0:
                    conflicts +=1
                    
                    
        return conflicts
    
        
    def result(self,state,action):
        queen,next_position=action
        new_state=list(state)
        new_state[queen]=next_position
        return new_state
    
    def successors(self,state):
        return [(self.result(state,a),a) for a in self.action(state)]
    
    def cost(self,state,action):
        return 1
    
    def value(self,state):
        return self.max_conflicts - self.conflits(state)
    
    def goal_test(self,state):
        return self.conflits(state)==0
    
    def random(self):
        return [random.randrange(0,self.environment.height) 
                for _ in range(self.environment.n_queens)]
        
    @staticmethod
    def print_chess(state):
        print('\t', end='')
        for number in [1, 2, 3, 4, 5, 6, 7, 8]:
            print(f"|  {number}  ", end='')
        print('|', end='')
        print('\n\t_________________________________________________')

        for row, letter in zip(range(8), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']):
            print(letter + '\t', end='')
            print('|', end='')

            for queen in state:
                if queen == row:
                    print('  Q  ', end='')
                else:
                    print('     ', end='')
                print('|', end='')
            print('\n', end='')
            print('\t_________________________________________________')

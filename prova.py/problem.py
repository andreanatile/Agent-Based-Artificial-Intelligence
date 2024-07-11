class QueenEnvironment:
    def __init__(self,height,width,n_queen):
        self.height=height
        self.width=width
        self.n_queen=n_queen

class N_QueenProblem:
    def __init__(self,intial_state,goal_state,environment):
        self.initial_state=intial_state
        self.goal_state=goal_state
        self.environment=environment
        
        
    def action(self,state):
        actions=[]
        for queen in range(len(state)):
            rem_position=[position for position in 
                          range(self.environment.height) if position!=state[queen]]
            
            for possible_position in rem_position:
                actions.append((queen,rem_position))
                
                
        return actions
    
    def conflits(self,state):
        conflicts=0
        for queen in range(len(state)):
            rem_queens=[rem_queen for rem_queen in range(len(state)) if rem_queen!=queen]
            for rem_queen in rem_queens:
                if state[queen]==state[rem_queen]:
                    conflicts +=1
                    
                if abs(state[queen]-state[rem_queen])==abs(queen-rem_queen):
                    conflicts +=1
                    
                if abs(queen+state[queen])==abs(rem_queen+state[rem_queen]):
                    conflicts +=1
                    
                    
        return conflicts
    
    def result(self,state,action):
        
                
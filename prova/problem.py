import copy

class HanoiProblem:
    def __init__(self,n_disk):
        self.n_disk=n_disk
        self.initial_state={'A':[n for n in range(self.n_disk)],
                            'B':[],
                            'C':[]}
        
        self.goal_state={'A':[],
                        'B':[],
                        'C':[n for n in range(self.n_disk)]}
        
    
    def actions(self,state):
        actions=[]
        
        for rod in list(state.keys()):
            rem_rods=[r for r in list(state.keys()) if r!=rod]
            for rem_rod in rem_rods:
                if state[rod]!=[]:
                    if state[rem_rod]==[] or state[rod][0]<state[rem_rod][0]:
                        actions.append((rod,rem_rod))
                    
        return actions
    
    
    def result(self,state,action):
        new_state=copy.deepcopy(state)
        rod,next_rod=action
        disk=new_state[rod].pop(0)
        new_state[next_rod]=[disk]+new_state[next_rod]
        return new_state
    
    def successors(self,state):
        return [(self.result(state,a),a) for a in self.actions(state)]
    
    def cost(self,state,action):
        return 1
    
    def goal_test(self,state):
        return state==self.goal_state
    
    def h(self,state):
        return (len(state['A']))**2+(len(state['B']))**2
    
    def value(self,state):
        return (self.n_disk**2-len(state['A']**2)-len(state['B']**2))
    
    
    def __repr__(self):
        return 'Hanoi problem'
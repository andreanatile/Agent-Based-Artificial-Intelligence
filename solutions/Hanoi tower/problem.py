import copy
class HanoiProblem:
    def __init__(self,n_disk=3):
        self.n_disk=n_disk
        self.initial_state={'A':[disk for disk in range(1,n_disk+1)],
                            'B':[],
                            'C':[]}
        self.goal_state={'A':[],'B':[],
                         'C':[disk for disk in range(1,n_disk+1)]}
        
    def goal_test(self,state):
        return state==self.goal_state
    
    def actions(self,state):
        #action will be a couple expressing the initial rod and the end rod
        actions=[]
        for rod in list(state.keys()):
            remaining_rods=[rem_rod for rem_rod in list(state.keys()) if rem_rod!=rod]
            for rem_rod in remaining_rods:
                if state[rod]!=[]:
                    if state[rem_rod]==[] or state[rod][0]<state[rem_rod][0]:
                        actions.append((rod,rem_rod))
                    
        return actions
    
    def result(self,state,action):
        rod,next_rod=action
        if state[rod]:
            new_state=copy.deepcopy(state)
            disk=new_state[rod].pop(0)
            new_state[next_rod]=[disk]+new_state[next_rod]
            return new_state
        
        raise ValueError('Unable to move the disk since rod is empty')
    
    def successors(self,state):
        return [(self.result(state,a),a) for a in self.actions(state)]
    
    def cost(self,state,action):
        return 1
    
    def h(self,state):
        return sum(state['A'])+sum(state['B'])
    
    def __repr__(self):
        return f'Hanoi problem'
            
    


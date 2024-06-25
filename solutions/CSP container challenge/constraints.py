"""
state={
    't1':0,
    't2':1
    ...
    }
"""

class Constraints:
    def __init__(self,variables):
        self.variables=variables
        
        
    def check(self,state):
        return False
    

class DifferentContainers(Constraints):
    def check(self,state):
        if self.variables[0] not in state or  self.variables[1] not in state:
            return True
        values=[state[var] for var in self.variables]
        return len(self.variables)==len(list(set(values)))
    
    def __repr__(self):
        return f'Different containers for {[var for var in self.variables]}'
    
class SameContainer(Constraints):
    def check(self,state):
        values=[state[var] for var in self.variables if var in state]
        return len(list(set(values)))==1
    
    def __repr__(self):
        return f'Same container for {[var for var in self.variables]}'

class NumberItemsConstraints:
    def __init__(self,limit,variables=[]):
        self.variables=variables
        self.limit=limit
        
    def check(self,state):
        count_containers={
            'C1':0,
            'C2':0,
            'C3':0,
            'C4':0
        }
        
        for value in list(state.values()):
            count_containers[value]+=1
            
        for container in list(count_containers.keys()):
            if count_containers[container]>self.limit:
                return False
        return True
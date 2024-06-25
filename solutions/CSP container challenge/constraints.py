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
    
class SameContainer(Constraints):
    def check(self,state):
        values=[state[var] for var in self.variables]
        return len(list(set(values)))==1


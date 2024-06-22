class Constraint:
    def __init__(self,variables):
        self.variables=variables
        
    def check(self,state):
        return False
    
    
class SameTable(Constraint):
    def check(self,state):
        if state[self.variables[0]]==state[self.variables[1]]:
            return True
        return False
    

class DifferentTable(Constraint):
    def check(self,state):
        if state[self.variables[0]]==state[self.variables[1]]:
            return False
        return True
    
class NumberChair(Constraint):
    def check(self,state):
        value_count={'A':0,
                     'B':0,
                     'C':0}
        
        for value in state.values():
            value_count[value] +=1
            
        if value_count['A']<=5 and value_count['B']<=5 and value_count['C']<=5:
            return True
        return False
        
        
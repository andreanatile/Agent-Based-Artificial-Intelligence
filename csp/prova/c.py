class Constraint:
    def __init__(self,variables):
        self.variables=variables
        self.degree=len(variables)
        
    def check(self,state):
        return False
    
    
class DifferentValues(Constraint):
    def check(self,state):
        values=[state[var] for var in self.variables if var in state]
        return len(set(values))==len(values)
    

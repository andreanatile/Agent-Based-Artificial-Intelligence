class Constraint:
    def __init__(self,variables):
        self.variables=variables
        
    def check(self,state):
        return False
    
    
    
"""
state={
    'tommaso':'B',
    'Giovanni':'C',
    ....
}

"""
class SameTable(Constraint):
    def check(self,state):
        if self.variables[0] in state and self.variables[1] in state:
            if state[self.variables[0]]!=state[self.variables[1]]:
                return False
            
        return True
    
    def __repr__(self):
        return f'Same table {self.variables[0]} and {self.variables[1]}'
    
class DifferentTable(Constraint):
    def check(self,state):
        if self.variables[0] in state and self.variables[1] in state:
            if state[self.variables[0]]==state[self.variables[1]]:
                return False
            
        return True
    
    def __repr__(self):
        return f'Different table {self.variables[0]} and {self.variables[1]}'
class NumberChairs:
    @staticmethod
    def check(state):
        chair_table={
            'A':0,
            'B':0,
            'C':0
        }
        
        for value in list(state.values()):
            if value in chair_table:
                chair_table[value] +=1
                
        if chair_table['A']>5 or chair_table['B']>5 or chair_table['C']>5:
            return False
        return True
class TableProblem:
    def __init__(self,variables,domains,constraints):
        self.variables=variables
        self.domains=domains
        self.constraints=constraints
        self.initial_state=dict()
        
    def consistent(self,state):
        return all([c.check(state) for c in self.constraints])
    
    def complete(self,state):
        return len(state)==len(self.variables)
    
    def goal_test(self,state):
        return self.consistent(state) and self.complete(state)
    
    def legal_moves(self,state,variable):
        possible_moves=self.domains[variable]
        return [move for move in possible_moves if self.consistent(self.assign(state,variable,move))]
    
    def assign(self,state,variable,value):
        if variable in self.variables and value in self.domains[variable]:
            new_state=dict(state)
            new_state[variable]=value
            return new_state
        
        raise ValueError
    
    def rol(self,state,variable):
        if variable in self.variables and variable in state:
            new_state=dict(state)
            del new_state[variable]
            return new_state
        
        raise ValueError
    
    def assignable_variables(self,state):
        return [var for var in self.variables if var not in state]
    
    def count_constraint(self,var1,var2):
        return sum([1 for c in self.constraints if 
                    var1 in c.variables and
                    var2 in c.variables])
        
    def remaining_constraints(self,state,variable):
        remeining_vars=[var for var in self.variables if var not in state and var!=variable]
        return sum([self.count_constraint(var,variable) for var in remeining_vars])
        
        
    
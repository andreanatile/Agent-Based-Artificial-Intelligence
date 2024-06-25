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
    
    def legal_moves(self,state,var):
        return [move for move in self.domains[var] if 
                self.consistent(self.assign(state,var,move))]
        
    def assign(self,state,var,value):
        if var in self.variables and value in self.domains[var]:
            new_state=dict(state)
            new_state[var]=value
            return new_state
        
        raise ValueError
    
    def rollback(self,state,var):
        if var in state and var in self.variables:
            new_statest=dict(state)
            del(new_statest[var])
            return new_statest

        raise ValueError
    
    def goal_test(self,state):
        return self.complete(state) and self.consistent(state)
    
    def count_constraints(self,first_var,second_var):
        return sum([1 for c in self.constraints if 
                    first_var in c.variables and 
                    second_var in c.variables])
        
    def remaining_constraints(self,state,variable):
        rem_var=[var for var in self.variables if var not in state and var!=variable]
        return sum([self.count_constraints(var,variable) for var in rem_var])
    
    def assignable_variables(self,state):
        return [var for var in self.variables if var not in state]
    
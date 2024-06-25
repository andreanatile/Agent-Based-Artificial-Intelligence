class ContainerProblem:
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
    
    def assign(self,state,variable,value):
        if variable in self.variables and value in self.domains[variable]:
            new_state=dict(state)
            new_state[variable]=value
            return new_state
        
        raise ValueError
    
    def rollback(sefl,state,variable):
        if variable in state:
            new_state=dict(state)
            del(new_state[variable])
            return new_state
        raise ValueError
    
    def legal_moves(self,state,variable):
        return [move for move in self.domains[variable] 
                if self.consistent(self.assign(state,variable,move))]
    
    def count_constraints(self,first_var,second_var):
        return sum([1 for c in self.constraints if 
                    first_var in c.variables and 
                    second_var in c.variables])
        
        
    def remaining_constraints(self,state,variable):
        rem_var=[var for var in self.variables if var not in state and var!=variable]
        
        return sum([self.count_constraints(var,variable) for var in rem_var])
    
    def assignable_variables(self,state):
        return [var for var in self.variables if var not in state]
    
    
class TableProblem:
    def __init__(self,variables,domains,constraints):
        self.variables=variables
        self.domains=domains
        self.constraints=constraints
        self.initial_state=dict()
        
    def consistents(self,state):
        return all([c.check(state) for c in self.constraints])
    
    def complete(self,state):
        return len(state.values())==15
    
    def assign(self,state,variable,value):
        if variable in self.variables and variable and value in self.domains[variable]:
            new_state=dict(state)
            new_state[variable]=value
            return new_state
        
        raise ValueError()
    
    def legal_moves(self,state,variable):
        possible_moves=self.domains[variable]
        return [move for move in possible_moves if self.consistents(self.assign(state,variable,move))]
    
    def roll_back(self,state,variable):
        if variable is self.variables and variable in state:
            new_state=dict(state)
            del new_state[variable]
            return new_state
        raise ValueError
    
    def assignable_variables(self,state):
        return [var for var in self.variables if var not in state]
    
    def count_constraints(self,first_var,second_var):
        return sum([1 for c in self.constraints if 
                    first_var in c.variables and 
                    second_var in c.variables])
        
    def remaining_constraints(self,state,variable):
        remaining_var=[var for var in self.variables if var not in state and var!=variable]
        return sum([self.count_constraints(var,variable) for var in remaining_var])
    
    def goal_test(self,state):
        return self.complete(state) and self.consistents(state)
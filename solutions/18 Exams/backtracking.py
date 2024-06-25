def minimum_remaining_values(problem,state):
    # Return the variable with the lowest legal moves
    return min(problem.assignable_variables(state),key=lambda var:
        len(problem.legal_moves(state,var)))
    
def degree_heuristic(problem,state):
    # Return the variable with the most constraint on remaining variable
    return max(problem.assignable_variables(state),key=lambda var:
        problem.remaining_constraints(state,var))
    
def least_constraining_value(problem,state,variable,domains):
    return sorted(domains[variable],key=lambda v:
        -sum([len(problem.legal_moves(problem.assign(state,variable,v),var))
              for var in problem.assignable_variables(problem.assign(state,variable,v))]))
    
    
class BackTracking:
    def __init__(self,problem,var_criterion,value_criterion):
        self.problem=problem
        self.var_criterion=var_criterion
        self.value_criterion=value_criterion
        
    def run(self,state):
        if self.problem.goal_test(state):
            return state
        
        var=self.var_criterion(self.problem,state)
        if var is None:
            return False
        
        values=self.value_criterion(self.problem,state,var,self.problem.domains)
        if values is None:
            return False
        
        
        for value in values:
            new_state=self.problem.assign(state,var,value)
            if self.problem.consistent(new_state):
                state=dict(new_state)
                result=self.run(dict(state))
                
                if result:
                    return result
                
                state=self.problem.rollback(state,var)
                
        return False
    
    def forward_check(self,state,domains):
        new_domains=dict(domains)
        for var in self.problem.assignable_variables(state):
            new_domains[var]=self.problem.legal_moves(state,var)
        return new_domains
    
    def run_with_forward_check(self,state,domains):
        
        if self.problem.goal_test(state):
            return state
        
        if [] in domains.values():
            return False
        
        var=self.var_criterion(self.problem,state)
        if var is None:
            return False
        
        values=self.value_criterion(self.problem,state,var,domains)
        if values is None:
            return False
        
        
        for value in values:
            new_state=self.problem.assign(state,var,value)
            if self.problem.consistent(new_state):
                new_domains=self.forward_check(state,domains)
                del(new_domains[var])
                
                state=dict(new_state)
                result=self.run(dict(state),new_domains)
                
                if result:
                    return result
                
                state=self.problem.rollback(state,var)
                
        return False
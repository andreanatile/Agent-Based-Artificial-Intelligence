
import random


def random_variable(problem, state):
    """
    Given a state returns a random assignable variable
    @param problem: a CSP problem
    @param state: a state
    @return: a random assignable variable
    """
    assignable_vars = problem.assignable_variables(state)
    if assignable_vars:
        random.shuffle(assignable_vars)
        return assignable_vars.pop()
    # if there are no assignable variables
    return None


def minimum_remaining_values(problem, state):
    """
    Choose the variable with the fewest legal values
    @param problem: a CSP problem
    @param state: a state
    @return: a variable
    """
    return min(problem.assignable_variables(state), key=lambda v: len(problem.legal_moves(state, v)))


def degree_heuristic(problem, state):
    """
    Choose the variable with the most constraints on remaining variables
    @param problem: a CSP problem
    @param state: a state
    @return: a variable
    """
    return max(problem.assignable_variables(state), key=lambda v: problem.remaining_constraints(state, v))


def random_assignment(problem, state, variable, domains):
    """
    Return a random value to be assigned to the variable
    @param problem: a CSP problem
    @param variable: a variable
    @return: a value for the variable
    """
    possible_values = domains[variable]
    random.shuffle(possible_values)
    return possible_values


def least_constraining_value(problem, state, variable, domains):
    """
    Given a variable, choose the least constraining value
    @param problem: a CSP problem
    @param state: a state
    @param variable: an assignable variable
    @return: a list of assignable values
    """
    assignable_values = domains[variable]
    return sorted(assignable_values,
                  key=lambda v: -sum([len(problem.legal_moves(problem.assign(state, variable, v), var))
                                      for var in problem.assignable_variables(problem.assign(state, variable, v))]))
class BackTracking:
    def __init__(self,problem,value_criterion=None,var_criterion=None):
        self.problem=problem
        self.value_criterion=value_criterion
        self.var_criterion=var_criterion
        
        
    def run(self,state):
        if self.problem.goal_test(state):
            return state
        
        var=self.var_criterion(self.problem,state)
        if var is None:
            raise ValueError('No variable to select')
        
        values=self.value_criterion(self.problem,state,var,self.problem.domains)
        if values is None:
            raise ValueError('No Values to select')
        
        for value in values:
            new_state=self.problem.assign(state,var,value)
            if self.problem.consistent(new_state):
                state=dict(new_state)
                
                result=self.run(dict(state))
                if result:
                    return result
                
                state=self.problem.rollback(state,var)
        
        raise ValueError('No result found')
                
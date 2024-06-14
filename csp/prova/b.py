def minimum_remaining_values(problem,state):
    return min(problem.assignable_variables(),
               key=lambda x:len(problem.legal_moves(state,x)))
    
def degree_heuristic(problem,state):
    return max(problem.assignable_variables(),
               key=lambda x:problem.remaining_constraints(state,x))
    
def least_constraining_value(problem,state,variable,domains):
    assignable_values = domains[variable]
    return sorted(assignable_values,
                  key=lambda v: -sum([len(problem.legal_moves(problem.assign(state, variable, v), var))
                                      for var in problem.assignable_variables(
                                          problem.assign(state, variable, v))]))
from problem import ContainerProblem
from backtracking import *

problem=ContainerProblem()
search=BackTracking(problem=problem,value_criterion=least_constraining_value,var_criterion=degree_heuristic)

result=search.run({})

print(result)
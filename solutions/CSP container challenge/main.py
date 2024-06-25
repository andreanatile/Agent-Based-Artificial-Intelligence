from constraints import *
from search import *
from problem import ContainerProblem


"""
state={
    't1':'C1'
}
"""

variables=['t1', 't2', 't3', 't4', 't5','f1', 'f2', 'f3',
 'e1','e2 ','fz1', 'fz2', 'fz3','fs1']

domains={var:['C1','C2','C3','C4'] for var in variables}

constraint=([DifferentContainers(['e1','e2']),DifferentContainers(['e2','e1'])]+
            [DifferentContainers([food,trash]) for food in ['f1', 'f2', 'f3'] 
             for trash in ['t1', 't2', 't3', 't4', 't5']] +
            [SameContainer(['fz1', 'fz2', 'fz3','fs1'])]+
            [DifferentContainers(['fs1',frozen]) for frozen in ['fz1', 'fz2', 'fz3','fs1']]+
            [NumberItemsConstraints(6)])

problem=ContainerProblem(variables=variables,domains=domains,constraints=constraint)
search=BackPropagation(problem=problem,var_criterion=degree_heuristic,value_criterion=least_constrain_values)
result=search.run_with_forward_check({},problem.domains)
print(result)
from backtracking import *
from problem import TableProblem
from constraint import *

variables=['Tommaso','Giovanni','Mario','Sergio','Vincenzo','Pietro','Andrea'
          'Rocco','Ivan','Domenico','Silvia',
          'Cofano','Tania','Filippo','Giuseppe']

domains={var:['A','B','C'] for var in variables}

constraints=[
    [SameTable([prof1,prof2]) for prof1 in ['Tommaso','Giovanni','Mario','Sergio']
     for prof2 in ['Tommaso','Giovanni','Mario','Sergio'] if prof1!=prof2 ]+
    [DifferentTable([phd1,phd3]) for phd1 in ['Vincenzo','Pietro','Andrea']
     for phd3 in ['Cofano','Tania','Filippo']]+[NumberChair(variables=[])]   
]

problem=TableProblem(variables=variables,domains=domains,constraints=constraints)

search=BackTracking(problem=problem,var_criterion=minimum_remaining_values,value_criterion=least_constraining_value)
state=search.run(problem.initial_state)
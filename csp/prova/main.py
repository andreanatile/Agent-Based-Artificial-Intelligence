from c import *
from p import *
import random
from b import *

problem=MapColors()
random.seed(42)

state={
    var:random.choice(problem.domains[var]) for var in random.choices(problem.variables,k=4)
}
print(state)

#print(problem.remaining_constraints(state,'WA'))
print(problem.assignable_variables(state))
print(least_constraining_value(problem=problem,state=state,variable='SA',domains=problem.domains))

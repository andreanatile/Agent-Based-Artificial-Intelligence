from local_search import *
from problem import *

environment=QueenEnvironment(height=8,n_queens=8)

problem=N_QueenProblem(environment=environment)

search=SimulatedAnneling(problem=problem,min_temp=0,max_time=100,lam=0.1)
message,result=search.run(initial_temp=100)
problem.print_chess(result)
print(' \nResult of Simulated Annealing:')
print(result)
print(f'Number of conflicts:{problem.conflits(result)}')
print('\n\n ------------------------------------------------ \n\n')

#-------------------Genetic-------------------

gene_pool=[_ for _ in range(environment.height)]
search = Genetic(problem=problem, population=1,generation=1,p_mutation=0.1,gene_pool=gene_pool)
result = search.run()
problem.print_chess(result)
print(' \nResult of Genetic Search:')
print(result)
print(f'Number of conflicts:{problem.conflits(result)}')
print('\n\n ------------------------------------------------ \n\n')
# -------------------Hill Climbing-------------------

search = HillClimbing(problem=problem)
result = search.run()
problem.print_chess(result)
print(' \nResult of Hill Climbing:')
print(result)
print(f'Number of conflicts:{problem.conflits(result)}')

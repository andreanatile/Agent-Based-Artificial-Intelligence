from problem import HanoiProblem
from graphSearch import GraphSearch
from strategy import *

problem=HanoiProblem(n_disk=3)
strategies=[DepthFirst(),Astar(problem)]


for strategy in strategies:
    search=GraphSearch(problem=problem,strategy=strategy)
    print(f'{search} with {strategy}')
    message,result=search.run()
    print(message)
    print(result.state)
    print(result.path())
    
    print('------------------------------------------------\n')
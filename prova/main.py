from graphsearch import GraphSearch
from treesearch import TreeSearch
from strategy import *
from problem import HanoiProblem


problem=HanoiProblem(n_disk=3)
strategies=[BreadthFirst(),DepthFirst(),Greedy(problem=problem),Astar(problem=problem)]

for strat in strategies:
    search=GraphSearch(problem,strat)
    message,result=search.run()
    if message != 'fail':
        print(search)
        print(result)
        print(result.path())
        print(f'Number of moves: {len(result.path())}')
    else:
        print(search)
        print(message)
    
    print('-----------------------------------')        
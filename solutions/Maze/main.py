from problem import *
from graphsearch import GraphSearch
from strategy import *
from node import Node

environment=MazeEnvironment(width=5,height=5,n_walls=2,p_walls=[(2,2),(2,3)])
problem=MazeProblem(initial_state=(0,0),goal_state=(4,4),environment=environment)

strategies=[BreadthFirst(),DepthFirst(),Astar(problem=problem)]

for strategy in strategies:
    search=GraphSearch(problem=problem,strategy=strategy)
    message,result=search.run()
    print(f'{search} with {strategy}')
    print(message)
    print(f'Number of moves {len(result.path())}')
    environment.display_maze(problem.intial_state,problem.goal_state,result.path_state())

    
    
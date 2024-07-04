class BreadthFirst:
    @staticmethod
    def select(fringe):
        node = fringe.pop(0)
        return fringe, node

    def __repr__(self):
        return 'Breadth first strategy'


class DepthFirst:
    @staticmethod
    def select(fringe):
        node = fringe.pop(0)
        return fringe, node

    def __repr__(self):
        return 'Depth first strategy'


class UniformCost:
    @staticmethod
    def select(fringe):
        fringe=sorted(fringe,key=lambda node:node.cost)
        node = fringe.pop(0)
        return fringe, node

    def __repr__(self):
        return 'Uniform cost strategy'
    

class Greedy:
    def __init__(self,problem):
        self.problem=problem
        
    def select(self,fringe):
        fringe = sorted(fringe, key=lambda node: self.problem.h(node.state))
        node = fringe.pop(0)
        return fringe, node

    def __repr__(self):
        return 'Greedy strategy'


class Astar:
    def __init__(self, problem):
        self.problem = problem

    def select(self, fringe):
        fringe = sorted(fringe, key=lambda node: (self.problem.h(node.state)+node.cost))
        node = fringe.pop(0)
        return fringe, node

    def __repr__(self):
        return 'Astar strategy'


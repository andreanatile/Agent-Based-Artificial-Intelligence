class DepthFirst:
    @staticmethod
    def select(fringe):
        node=fringe.pop(0)
        return fringe,node
    def __repr__(self):
        return f'Depth First strategy'
    
class Astar:
    def __init__(self,problem):
        self.problem=problem
        
    def select(self,fringe):
        fringe=sorted(fringe,key=lambda node:(node.cost+self.problem.h(node.state)))
        node=fringe.pop(0)
        return fringe,node
    
    def __repr__(self):
        return f'Astar strategy'

        
        

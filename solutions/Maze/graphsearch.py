from node import Node

class GraphSearch:
    def __init__(self,problem,strategy):
        self.problem=problem
        self.strategy=strategy
        self.fringe=[]
        self.visited=[]
        
    def run(self):
        node=Node(state=self.problem.intial_state,
                  parent=None,
                  cost=0,
                  action=None,
                  depth=0)
        
        while True:
            if self.problem.goal_test(node.state):
                return 'ok',node
            
            self.visited.append(node.state)
            
            new_nodes=[node.expand(s,a,self.problem.cost(s,a))
                       for s,a in self.problem.successors(node.state)]
            
            new_nodes=[n for n in new_nodes if n.state not in self.visited]
            self.fringe=[n for n in self.fringe if n.state not in self.visited]
            
            self.fringe=self.fringe+new_nodes
            
            if len(self.fringe)!=0:
                self.fringe,node=self.strategy.select(self.fringe)
                if node is None:
                    return 'fail',[]
                
            else:
                if self.problem.goal_test(node.state):
                    return 'ok',node
                else:
                    return 'fail',[]
                
                
    def __repr__(self):
        return f'Graph Search'
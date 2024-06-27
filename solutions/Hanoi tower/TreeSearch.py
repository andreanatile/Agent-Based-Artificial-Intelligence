from node import Node
class TreeSearch:
    def __init__(self,problem,strategy):
        self.problem=problem
        self.strategy=strategy
        self.fringe=[]
        
    def run(self):
        node=Node(state=self.problem.initial_state,
                  action=None,
                  parent=None,
                  cost=0,
                  depth=0)
        
        while True:
            if self.problem.goal_test(node.state):
                return 'ok',node
            
            new_states=[node.expand(state=s,action=a,cost=self.problem.cost(s,a)) 
                        for s,a in self.problem.successors(node.state)]
            
            self.fringe=self.fringe+new_states
            
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
        return f'Tree Search'
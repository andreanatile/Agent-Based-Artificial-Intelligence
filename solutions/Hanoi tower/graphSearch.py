from node import Node
class GraphSearch:
    def __init__(self,problem,strategy):
        self.problem=problem
        self.strategy=strategy
        self.fringe=[]
        self.visited=[]
        
    def run(self):
        node=Node(state=self.problem.initial_state,
                  action=None,
                  parent=None,
                  cost=0,
                  depth=0)
        
        while True:
            if self.problem.goal_test(node.state):
                return 'ok',node
            
            self.visited.append(node.state)
            
            new_states=[node.expand(state=s,action=a,cost=self.problem.cost(s,a)) 
                        for s,a in self.problem.successors(node.state)]
            
            new_states=[n for n in new_states if n.state not in self.visited]
            self.fringe=[n for n in self.fringe if n.state not in self.visited]
            
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
        return f'Graph Search'
class Node:
    def __init__(self,state,action,parent,cost,depth):
        self.state=state
        self.action=action
        self.parent=parent
        self.cost=cost
        self.depth=depth
        
        
    def expand(self,state,action,cost):
        return Node(state=state,
                    action=action,
                    parent=self,
                    cost=self.cost+cost,
                    depth=self.depth+1)
        
    def path(self):
        path=[]
        node=self
        
        while node.parent:
            path.append(node.action)
            node=node.parent
            
        path=list(reversed(path))
        return path
    
    def __repr__(self):
        return f'Node {self.state}'
    
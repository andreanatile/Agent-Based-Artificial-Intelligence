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
                    cost=self.cost+cost,
                    parent=self,
                    depth=self.depth+1)
        
    def path(self):
        path=[]
        node=self
        
        while node.parent:
            path.append(node.action)
            node=node.parent
            
        path=list(reversed(path))
        return path
    
    def path_state(self):
        path=[]
        node=self
        
        while node.parent:
            path.append(node.state)
            node=node.parent
            
        path=list(reversed(path))
        return path
    
    def __repr__(self):
        return f'Node state: {self.state}'
    
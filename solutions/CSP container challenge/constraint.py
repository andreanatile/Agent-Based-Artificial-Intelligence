
class Constraint:
    def __init__(self,variables):
        self.variables=variables
        
    def check(self,state):
        return False
    
    
class DifferentContainter(Constraint):
    def check(self,state):
        values=[state[var] for var in self.variables if var in state]
        return len(values)==len(set(values))
    
    
class SameContainer(Constraint):
    def check(self,state):
        values=[state[var] for var in self.variables if var in state]
        if values:
            return len(set(values))==1
        return True
    
class LimitContainer(Constraint):
    def __init__(self,maxcapacity,variables=[]):
        super().__init__(variables)
        self.maxCapacity=maxcapacity
        
    def check(self,state):
        count_item={'C1':0,
                    'C2':0,
                    'C3':0,
                    'C4':0}
        
        for value in list(state.values()):
            count_item[value] +=1
        
        for container in list(count_item.keys()):
            if count_item[container]>self.maxCapacity:
                return False
            
        return True
    
class UnaryConstraint(Constraint):
    def __init__(self, variable):
        self.variable = variable
        super(UnaryConstraint, self).__init__(variables=variable)

    def check(self, state):
        return True
    
class MaximumCapacity(UnaryConstraint):
    def __init__(self, variable, max_capacity):
        super(MaximumCapacity, self).__init__(variable)
        self.maxCapacity = max_capacity

    def check(self, state):
        values = [state[var] for var in self.variables if var in state]
        return all([values.count(x) <= self.maxCapacity for x in values])
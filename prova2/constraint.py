class Constraint:
    def __init__(self, variables):
        self.variables = self.variables

    def check(self, state):
        return False


class DifferentValue(Constraint):
    def check(self, state):
        values = [state[var] for var in self.variables if var in state]

        if values:
            return len(values) == len(set(values))
        else:
            True


class SameValue(Constraint):
    def check(self, state):
        values = [state[var] for var in self.variables if var in state]

        if values:
            return len(set(values)) == 1
        else:
            True

class MaxCapacity(Constraint):
    def __init(self,variables,max_capacity,n_containers):
        super(MaxCapacity,self).__init__(variables)
        self.max_capacity=max_capacity
        self.n_containers=n_containers
        
    def check(self,state):
        count_items={f'C{x}':0 for x in range(1,self.n_containers)}
        
        for value in list(state.values()):
            count_items[value] +=1
            
        for var in list(count_items.keys()):
            if count_items[var]>self.max_capacity:
                return False
        
        return True
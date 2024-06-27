from constraint import *
class CSP:
    def __init__(self,variables,domains,constraints):
        self.domains=domains
        self.variables=variables
        self.constraints=constraints
        self.initial_state=dict()
        
        
    def consistent(self,state):
        return all([c.check(state) for c in self.constraints])
    
    def complete(self,state):
        return len(state)==len(self.variables)
    
    def goal_test(self,state):
        return self.consistent(state) and self.complete(state)
    
    def assign(self,state,variable,value):
        if variable  in self.variables and value in self.domains[variable]:
            new_state=dict(state)
            new_state[variable]=value
            return new_state
        
        raise ValueError('Illegal Assignement')
    
    def rollback(self,state,variable):
        if variable in self.variables:
            new_state=dict(state)
            del new_state[variable]
            return new_state
        
        raise ValueError('Illegal Rollback')
    
    def legal_moves(self,state,variable):
        moves=self.domains[variable]
        return [move for move in moves if self.consistent(self.assign(state,variable,move))]
    
    def count_constraints(self,first_var,second_var):
        return sum([1 for c in self.constraints if first_var is c.variables
                    and second_var in c.variables])
        
    def remaining_constraints(self,state,variable):
        rem_var=[var for var in self.variables if var not in state and var!=variable]
        if rem_var:
            return sum([self.count_constraints(variable,var) for var in rem_var])
        return 0
    
    def assignable_variables(self,state):
        return [var for var in self.variables if var not in state]
    
class ContainerProblem(CSP):
    def __init__(self):
        self.variables=['t1', 't2', 't3','t4', 't5', 'f1', 'f2', 'f3', 'e1', 'e2', 'fz1',
         'fz2', 'fz3', 'fs1']
        self.domains={var:['C1','C2','C3','C4'] for var in self.variables}
        self.constraints=([DifferentContainter(['e1','e2']),DifferentContainter(['e2','e1'])] +
                          [DifferentContainter([food,trash]) for food in ['f1', 'f2', 'f3']
                           for trash in ['t1', 't2', 't3','t4', 't5']]+
                          [DifferentContainter([trash,food]) for food in ['f1', 'f2', 'f3']
                           for trash in ['t1', 't2', 't3','t4', 't5']]+
                          [SameContainer(['fz1','fz2', 'fz3'])]+
                          [DifferentContainter([frozen,'fs1']) for frozen in [ 'fz1','fz2', 'fz3']]+
                          [DifferentContainter(['fs1',frozen]) for frozen in [ 'fz1','fz2', 'fz3']]+
                          [MaximumCapacity(self.variables,max_capacity=6)])
        

         
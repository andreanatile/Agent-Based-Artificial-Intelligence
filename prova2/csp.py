from constraint import *


class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.initial_state = dict()

    def consistent(self, state):
        return all([c.check(state) for c in self.constraints])

    def complete(self, state):
        return len(state) == len(self.variables)

    def goal_test(self, state):
        return self.complete(state) and self.consistent(state)

    def assign(self, state, variable, value):
        if variable in self.variables and value in self.domains[variable]:
            new_state = dict(state)
            new_state[variable] = value
            return new_state

        raise ValueError()

    def rollback(self, state, variable):
        if variable in self.variables and variable in state:
            new_state = dict(state)
            del new_state[new_state]
            return new_state
        raise ValueError()

    def legal_moves(self, state, variable):
        possible_values = self.domains[variable]

        return [v for v in possible_values if
                self.consistent(self.assign(state, variable, v))]

    def count_constraints(self, first_var, second_var):
        return sum([1 for c in self.constraints
                    if first_var in c.variables and
                    second_var in c.variables])

    def remaining_constraints(self, state, variable):
        rem_var = [var for var in self.variables
                   if var not in state and var != variable]
        if rem_var:
            return sum([self.count_constraints(var, variable) for var in rem_var])
        else:
            return 0

    def assignable_variables(self, state):
        return [var for var in self.variables if var not in state]


class ContainerProblem(CSP):
    def __init__(self, n_containers):
        variables = ['t1', 't2', 't3', 't4', 't5',
                     'f1', 'f2', 'f3', 'e1', 'e2',
                     'fz1', 'fz2', 'fz3', 'fs1']

        domains = {var: [f'C{x}' for x in range(1, n_containers+1)]
                   for var in variables}

        constraints = ([DifferentValue(['e1', 'e2']), DifferentValue(['e2', 'e1'])]+[
            DifferentValue([trash, food]) for trash in ['t1', 't2', 't3', 't4', 't5']
            for food in ['f1', 'f2', 'f3']]+[
                DifferentValue([food,trash]) for trash in ['t1', 't2', 't3', 't4', 't5']
            for food in ['f1', 'f2', 'f3']
            ]+[SameValue(['fz1', 'fz2', 'fz3'])]+[
                DifferentValue([frozen, 'fs1']) for frozen in ['fz1', 'fz2', 'fz3']
            ]+[
                DifferentValue(['fs1',frozen]) for frozen in ['fz1', 'fz2', 'fz3']
            ])
        
        super(ContainerProblem,self).__init__(variables,domains,constraints)

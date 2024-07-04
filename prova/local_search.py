from node import Node
import random
import math


class HillClimbing:
    def __init__(self, problem):
        self.problem = problem

    def run(self):
        node = Node(self.problem.initial_state,
                    action=None,
                    parent=None,
                    cost=0,
                    depth=0)

        while True:
            new_state = self.problem.successors(node.state)
            if not new_state:
                return 'stop', node.state

            best_neighbour, best_action = max(
                new_state, key=lambda x: self.problem.value(x[0]))

            if self.problem.value(best_neighbour) <= self.problem.value(node.state):
                return 'ok', node.state

            node = node.expand(state=best_neighbour,
                               action=best_action,
                               cost=0)


class SimulatedAnnealing:
    def __init__(self, problem, min_temp=0, max_time=100, lam=1e-2):
        self.problem = problem
        self.min_temp = min_temp
        self.max_time = max_time
        self.lam = lam

    def exponenitalSchedule(self, temp, time):
        return temp * math.exp(-time*self.lam)

    def run(self, intial_temp=100):
        node = Node(self.problem.initial_state,
                    action=None,
                    parent=None,
                    cost=0,
                    depth=0)

        temp = intial_temp
        time = 0

        while time < self.max_time and temp > self.min_temp:

            selected_neighbour, selected_action = random.choice(
                self.problem.successors(node.state))

            score_diff = self.problem.value(
                selected_neighbour)-self.problem.value(node.state)

            if score_diff > 0 or random.uniform(0, 1) < math.exp(score_diff/temp):
                node = node.expand(state=selected_neighbour,
                                   action=selected_action, cost=0)

            temp = self.exponenitalSchedule(temp, time)
            time += 1

        return node.state


class Genetic:
    def __init__(self, problem, population, generation, p_mutation, gene_pool):
        self.problem = problem
        self.population = population
        self.generation = generation
        self.p_mutation = p_mutation
        self.gene_pool = gene_pool

    def select(self, population):
        fitnesess = list(map(self.problem.value, population))
        return random.choices(population=population, weights=fitnesess, k=2)

    def crossover(self, couple):
        first, second = couple
        split = random.randrange(0, len(first))

        return tuple(list(first[:split])+list(second[split:]))

    def mutation(self, state):
        if random.uniform(0, 1) > self.p_mutation or self.gene_pool is None:
            return state

        new_state = list(state)
        new_state[random.randrange(0, len(state))
                  ] = random.choice(self.gene_pool)
        return tuple(new_state)

    def run(self):
        population = [self.problem.random() for _ in range(self.population)]
        for e in self.generation:
            new_generation = [
                self.mutation(
                    self.crossover(
                        self.select(population)
                    )
                )
                for _ in range(self.population)]

            population = new_generation

        return max(population, key=lambda x: self.problem.value(x))

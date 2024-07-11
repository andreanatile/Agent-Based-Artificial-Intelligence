from Node import Node
import math
import random


class HillClimbing:
    def __init__(self,problem):
        self.problem=problem
        
        
    def run(self):
        node=Node(state=self.problem.initial_state,
                  parent=None,
                  action=None,
                  cost=0,
                  depth=0)
        
        while True:
            new_states=self.problem.successors(node.state)
            
            if not new_states:
                return False
            
            best_state,best_action=max(new_states,
                                       key=lambda s:self.problem.value(s))
            
            if self.problem.value(best_state)<=self.problem.value(node.state):
                return node.state
            
            node=node.expand(state=best_action,action=best_action)
                
                
class SimulatedAnneling:
    def __init__(self,problem,max_time,min_temp,lam):
        self.problem=problem
        self.max_time=max_time
        self.min_temp=min_temp
        self.lam=lam
        
    def exponential_schedule(self,temp,time):
        return temp*math.exp(-self.lam*time)
    
    def linear_schedule(self,temp):
        return temp-self.lam
    
    def proportional_schedule(self,temp):
        return temp-self.lam*temp
    
    def run(self,initial_temp):
        node = Node(state=self.problem.initial_state,
                    parent=None,
                    action=None,
                    cost=0,
                    depth=0)
        
        temp=initial_temp
        time=0
        
        while time<self.max_time and temp>self.min_temp:
            new_states = self.problem.successors(node.state)

            if not new_states:
                return False
            
            selected_state,selected_action=random.choice(new_states)
            
            score_diff=self.problem.value(selected_state)-self.problem.value(node.state)
            
            if score_diff>0 or random.uniform(0,1)<math.exp(score_diff/temp):
                node=node.expand(state=selected_state,action=selected_action)
                
            temp=self.exponential_schedule(temp,time)
            time +=1
            
        return node.state
    
    
class Genetic:
    def __init__(self,problem,population,generation,p_mutation,gene_pool):
        self.problem=problem
        self.population=population
        self.generation=generation
        self.p_mutation=p_mutation
        self.gene_pool=gene_pool
        
    def select(self,population):
        fitnesses=list(map(self.problem.value,population))
        return random.choices(population=population,weights=fitnesses,k=2)
    
    def crossover(self,couple):
        parent_a,parent_b=couple
        split=random.randrange(len(parent_a))
        
        return tuple(list(parent_a[:split])+list(parent_b[split:]))
    
    def mutation(self,state):
        if self.gene_pool is None or random.uniform(0,1)>self.p_mutation:
            return state
        
        state[random.randrange(len(state))]=random.choice(self.gene_pool)
        return tuple(state)
    
        
        
    def run(self):
        population=[self.problem.random() for _ in range(self.population)]
        for e in range(self.generation):
            new_generation=[
                self.mutation(
                    self.crossover(
                        self.select(population)
                    )
                )
             for _ in range(self.population)]
            
            population=new_generation
            
        return max(population,key=lambda x:self.problem.value(x))
    
    
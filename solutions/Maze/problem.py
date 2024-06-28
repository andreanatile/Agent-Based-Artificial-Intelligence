import numpy as np
class MazeProblem:
    def __init__(self,initial_state,goal_state,environment):
        self.intial_state=initial_state
        self.goal_state=goal_state
        self.environment=environment

        

    def action(self,state):
        actions=['up','down','left','right']
        if state[1]==0:
            actions.remove('left')
        if state[1]==(self.environment.width-1):
            actions.remove('right')
            
        if state[0]==0:
            actions.remove('up')

        if state[0]==(self.environment.height-1):
            actions.remove('down')
        
        for wall in self.environment.p_walls:
            if state==(wall[0],wall[1]-1):
                actions.remove('right')
                
            if state==(wall[0],wall[1]+1):
                actions.remove('left')
                
            if state==(wall[0]-1,wall[1]):
                actions.remove('down')
                
            if state==(wall[0]+1,wall[1]):
                actions.remove('up')
                
        return actions
            
    
    def result(self,state,action):
        if action=='right':
            return (state[0],state[1]+1)
        
        if action=='left':
            return (state[0],state[1]-1)
        
        if action=='up':
            return (state[0]-1,state[1])
        
        if action=='down':
            return (state[0]+1,state[1])
        
        raise ValueError(f'No legal Action: {action}')
    
    def successors(self,state):
        return [(self.result(state,a),a) for a in self.action(state)]
    
    def goal_test(self,state):
        return state==self.goal_state
    
    def cost(self,state,action):
        return 1
    
    def h(self,state):
        return (self.goal_state[0]-state[0])^2+(self.goal_state[1]-state[1])^2
    
    

class MazeEnvironment:
    def __init__(self,width,height,n_walls,p_walls):
        self.width=width
        self.height=height
        self.n_walls=n_walls
        self.p_walls=p_walls
        
    def display_maze(self,initial_state,goal_state,path_state):
        maze=[['| |' for _ in range(self.width)] for __ in range(self.height)]
        for state in path_state:
            maze[state[0]][state[1]]='|*|'
        for wall in self.p_walls:
            maze[wall[0]][wall[1]]='|o|'
            
        maze[initial_state[0]][initial_state[1]]='|i|'
        maze[goal_state[0]][goal_state[1]]='|g|'
        
        for i in range(self.height):
            print(maze[i])
            print('-----------------------------------')
            
        
        
        
        
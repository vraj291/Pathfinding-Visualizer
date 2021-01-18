import random
import sys
sys.path.insert(1,'d:/python samples/')
from pathfinding_visualizer.generate.maze.basemaze import BaseMaze

class RecursiveBacktracking(BaseMaze):

    def __init__(self,frame,canvas,algo):
        BaseMaze.__init__(self,frame,canvas,algo)  
        self.generatemaze()

    def generatemaze(self):
        self.track.append([random.randrange(1,self.leng+1,2),random.randrange(1,self.bre+1,2)])
        while len(self.track) != 0:
            curr=self.track[-1]
            neighbours=self.findNeighbours(curr[0]-1,curr[1]-1)
            if len(neighbours) == 0:
                self.track.pop(-1)
            else:
                rand=neighbours[0]
                self.can.create_rectangle(rand[0]*self.size,rand[1]*self.size,(rand[0]+1)*self.size,(rand[1]+1)*self.size,fill='white')
                self.can.create_rectangle((rand[0]+curr[0])//2*self.size,(rand[1]+curr[1])//2*self.size,(((rand[0]+curr[0])//2)+1)*self.size,(((rand[1]+curr[1])//2)+1)*self.size,fill='white')
                self.graph.grid[rand[0]-1][rand[1]-1].isBlock=False
                self.graph.grid[(rand[0]+curr[0])//2 -1][(rand[1]+curr[1])//2 -1].isBlock=False
                self.isVisited[rand[0]-1][rand[1]-1]=True
                self.isVisited[(rand[0]+curr[0])//2 -1][(rand[1]+curr[1])//2 -1]=True
                self.track.append(rand)
    
    

    

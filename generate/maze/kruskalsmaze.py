import random
from numpy.random import shuffle
import sys
sys.path.insert(1,'d:/python samples/')
from pathfinding_visualizer.generate.maze.basemaze import BaseMaze

class KruskalsAlgo(BaseMaze):

    def __init__(self,frame,canvas,algo):
        BaseMaze.__init__(self,frame,canvas,algo)
        self.forest=[]
        self.edges=[]
        for i in range(1,self.leng+1,2):
            for j in range(1,self.bre+1,2):
                self.forest.append([(i,j)])
                self.graph.grid[i-1][j-1].isBlock=False
                self.can.create_rectangle(i*self.size, j*self.size, (i+1)*self.size, (j+1)*self.size,fill='white')  
        for i in range(1,self.leng+1):
            for j in range(1,self.bre+1):
                if self.graph.grid[i-1][j-1].isBlock:
                    self.edges.append([i,j])
        shuffle(self.edges)
        self.generatemaze()
    
    def generatemaze(self):
        while len(self.forest)>1:
            rand=self.edges[0]
            self.edges=self.edges[1:]
            tree1=-1
            tree2=-1
            if rand[1] % 2 == 0:
                tree1=sum([i if (rand[0],rand[1]-1) in j else 0 for i,j in enumerate(self.forest)])
                tree2=sum([i if (rand[0],rand[1]+1) in j else 0 for i,j in enumerate(self.forest)])
            else:
                tree1=sum([i if (rand[0]-1,rand[1]) in j else 0 for i,j in enumerate(self.forest)])
                tree2=sum([i if (rand[0]+1,rand[1]) in j else 0 for i,j in enumerate(self.forest)])
            if tree1 != tree2:
                self.can.create_rectangle(rand[0]*self.size,rand[1]*self.size,(rand[0]+1)*self.size,(rand[1]+1)*self.size,fill='white')
                self.graph.grid[rand[0]-1][rand[1]-1].isBlock=False
                new_tree = self.forest[tree1] + self.forest[tree2]
                temp1 = list(self.forest[tree1])
                temp2 = list(self.forest[tree2])
                self.forest = [x for x in self.forest if x != temp1]
                self.forest = [x for x in self.forest if x != temp2]
                self.forest.append(new_tree)
            


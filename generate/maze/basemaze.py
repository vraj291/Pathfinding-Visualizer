import random
from numpy.random import shuffle
import sys
sys.path.insert(1,'d:/python samples/')
from pathfinding_visualizer.generate.baseframe import BaseFrame

class BaseMaze(BaseFrame):

    def __init__(self,frame,canvas,algo):
        BaseFrame.__init__(self,frame,canvas,algo)
        self.track=[]
        self.isVisited=[[False for x in range(self.bre)] for x in range(self.leng)] 
        self.preprocess() 

    def preprocess(self):
        for i in range(1,self.leng+1):
            for j in range(1,self.bre+1):
                self.graph.grid[i-1][j-1].isBlock=True
                self.can.create_rectangle(i*self.size, j*self.size, (i+1)*self.size, (j+1)*self.size,fill='black')

    def findNeighbours(self,x,y):
        neigh=[]        
        self.isVisited[x][y]=True
        if self.isValid(x+1,y-1) and not(self.isVisited[x][y-2]):
            neigh.append([x+1,y-1])
        if self.isValid(x-1,y+1) and not(self.isVisited[x-2][y]):
            neigh.append([x-1,y+1])
        if self.isValid(x+3,y+1) and not(self.isVisited[x+2][y]):
            neigh.append([x+3,y+1])
        if self.isValid(x+1,y+3) and not(self.isVisited[x][y+2]):
            neigh.append([x+1,y+3])
        shuffle(neigh)
        return neigh
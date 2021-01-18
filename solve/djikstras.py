import math
from pathfinding_visualizer.solve.pathfindingalgo import BaseAlgo
from tkinter import Tk,Frame,Canvas,BOTH 
import time

class djikstraspath(BaseAlgo):

    def __init__(self,canvas,con):
        BaseAlgo.__init__(self,canvas,con)

    def getDistance(self,x,y):
        return self.grid[x-1][y-1].d

    def setDistance(self,x,y,dis):
        self.grid[x-1][y-1].d = dis

    def setSource(self,source):
        self.setDistance(source.x,source.y,0)
    
    def setDestination(self,dest):
        self.setDistance(dest.x,dest.y,-1)

    def getNextNode(self):
        min=math.inf
        for x,y in self.open:
            if self.grid[x-1][y-1].d < min and not(self.isClosed(x,y)):
                min=self.grid[x-1][y-1].d
                min_index=[x,y]
        self.open.remove(min_index)
        return min_index

    def initializeNode(self,x,y):
        self.setDistance(x,y,math.inf)
        self.setParents(x,y,0,0)

    def resetBoard(self,source,dest):
        pc=self.precheck(source,dest)
        if not(pc[0]):
            self.con.enableButtons()
            return(pc[1])
        self.closed=[[False for x in range(self.bre)] for y in range(self.leng)]
        for i in range(1,self.leng+1):
            for j in range(1,self.bre+1):
                self.initializeNode(i,j)

    def isDestination(self,x,y):
        return self.grid[x-1][y-1].d == -1

    def findpath(self,source,dest):
        self.isComplete=False
        self.open=[]
        self.isComplete=False
        self.setDistance(source.x,source.y,0)
        self.setDistance(dest.x,dest.y,-1)
        self.open.append([source.x,source.y])
        if self.diag:
            while len(self.open) != 0 and not(self.isComplete):
                curr=self.getNextNode()
                for i in range(-1,2):
                    for j in range(-1,2):
                        if self.checkSuccessorsDiagonally(i,j) and self.isValid(curr[0]+i,curr[1]+j) :
                            if self.isDestination(curr[0]+i,curr[1]+j):
                                dest.parent_x=curr[0]
                                dest.parent_y=curr[1]
                                self.tracepath(source,dest)
                                self.con.enableButtons()
                                return('Path Found')
                            elif self.getDistance(curr[0]+i,curr[1]+j) > self.getDistance(curr[0],curr[1]) + 1  and not(self.isBlocked(curr[0]+i,curr[1]+j)) and not(self.isClosed(curr[0]+i,curr[1]+j)) :
                                self.setDistance(curr[0]+i,curr[1]+j,self.getDistance(curr[0],curr[1])+1)
                                self.setParents(curr[0]+i,curr[1]+j,curr[0],curr[1])
                                self.open.append([curr[0]+i,curr[1]+j])
                                self.paintOpen(curr[0]+i,curr[1]+j)
                self.closed[curr[0]-1][curr[1]-1]=True
                if curr[0]!=source.x or curr[1]!=source.y:
                    self.paintClosed(curr[0],curr[1])
        else:
            while len(self.open) != 0 and not(self.isComplete):
                curr=self.getNextNode()
                for i in range(-1,2):
                    for j in range(-1,2):
                        if self.checkSuccessors(i,j) and self.isValid(curr[0]+i,curr[1]+j) :
                            if self.isDestination(curr[0]+i,curr[1]+j):
                                dest.parent_x=curr[0]
                                dest.parent_y=curr[1]
                                self.tracepath(source,dest)
                                self.con.enableButtons()
                                return('Path Found')
                            elif self.getDistance(curr[0]+i,curr[1]+j) > self.getDistance(curr[0],curr[1]) + 1  and not(self.isBlocked(curr[0]+i,curr[1]+j)) and not(self.isClosed(curr[0]+i,curr[1]+j))  :
                                self.setDistance(curr[0]+i,curr[1]+j,self.getDistance(curr[0],curr[1])+1)
                                self.setParents(curr[0]+i,curr[1]+j,curr[0],curr[1])
                                self.open.append([curr[0]+i,curr[1]+j])
                                self.paintOpen(curr[0]+i,curr[1]+j)
                self.closed[curr[0]-1][curr[1]-1]=True
                if curr[0]!=source.x or curr[1]!=source.y:
                    self.paintClosed(curr[0],curr[1])
        if not(self.isComplete):
            self.con.enableButtons()
            return ('No Path Found')

            

    


   






from pathfinding_visualizer.solve.pathfindingalgo import BaseAlgo
import math

class Astarpathfinding(BaseAlgo):

    def __init__(self,canvas,con):
        BaseAlgo.__init__(self,canvas,con)
    
    def getFval(self,x,y):
        return self.grid[x-1][y-1].f

    def setFval(self,x,y,val=None):
        if val is None:
            self.grid[x-1][y-1].f = self.grid[x-1][y-1].g + self.grid[x-1][y-1].h
        else:
            self.grid[x-1][y-1].f = val

    def getGval(self,x,y):
        return self.grid[x-1][y-1].g

    def setGval(self,x,y,dis):
        self.grid[x-1][y-1].f = dis
    
    def getHval(self,x,y):
        return self.grid[x-1][y-1].h

    def setHvalEuclidean(self,x,y,dest):
        self.grid[x-1][y-1].h = math.sqrt((x-dest.x)**2+(y-dest.y)**2)
    
    def setHvalManhattan(self,x,y,dest):
        self.grid[x-1][y-1].h = abs(x-dest.x) + abs(y-dest.y)
 
    def setHvalDiagonal(self,x,y,dest):
        self.grid[x-1][y-1].h = max(abs(x-dest.x)+abs(y-dest.y))

    def setSource(self,source):
        self.open.append([source.x,source.y])
    
    def setDestination(self,dest):
        self.setFval(dest.x,dest.y,-1)

    def isDestination(self,x,y):
        return self.getFval(x,y) == -1

    def getNextNode(self):
        min=math.inf
        min_index=None
        for x,y in self.open:
            if self.getFval(x,y) <= min and not(self.isClosed(x,y)):
                min=self.getFval(x,y)
                min_index=[x,y]
        return min_index

    def initializeNode(self,x,y):
        self.grid[x-1][y-1].f=math.inf
        self.grid[x-1][y-1].g=1 
        self.grid[x-1][y-1].h=0
        self.grid[x-1][y-1].parent_x=0
        self.grid[x-1][y-1].parent_y=0

    def resetBoard(self,source,dest):
        pc=self.precheck(source,dest)
        if not(pc[0]):
            self.con.enableButtons()
            return(pc[1])
        self.closed=[[False for x in range(self.bre)] for x in range(self.leng)] 
        for i in range(1,self.leng+1):
            for j in range(1,self.bre+1):
                self.initializeNode(i,j)

    def findpath(self,source,dest):
        self.open=[]
        self.counter=0
        self.isComplete=False
        self.setSource(source)
        self.setDestination(dest)
        if not(self.diag):
            while len(self.open) != 0 and not(self.isComplete):
                curr=self.getNextNode()
                if curr is None:
                    break
                else:
                    self.open.remove(curr)
                for i in range(-1,2):
                    for j in range(-1,2):
                        if self.checkSuccessors(i,j) and self.isValid(curr[0]+i,curr[1]+j):
                            if self.isDestination(curr[0]+i,curr[1]+j):
                                dest.parent_x=curr[0]
                                dest.parent_y=curr[1]
                                self.tracepath(source,dest)
                                self.con.enableButtons()
                                return('Path Found')
                            elif not(self.isBlocked(curr[0]+i,curr[1]+j)) and not(self.isClosed(curr[0]+i,curr[1]+j)):
                                self.setHvalEuclidean(curr[0]+i,curr[1]+j,dest)
                                self.setFval(curr[0]+i,curr[1]+j)
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
                        if self.checkSuccessorsDiagonally(i,j) and self.isValid(curr[0]+i,curr[1]+j):
                            if self.isDestination(curr[0]+i,curr[1]+j):
                                dest.parent_x=curr[0]
                                dest.parent_y=curr[1]
                                self.tracepath(source,dest)
                                self.con.enableButtons()
                                return('Path Found')
                            elif not(self.isBlocked(curr[0]+i,curr[1]+j)) and not(self.isClosed(curr[0]+i,curr[1]+j)):
                                self.setHvalEuclidean(curr[0]+i,curr[1]+j,dest)
                                self.setFval(curr[0]+i,curr[1]+j)
                                self.setParents(curr[0]+i,curr[1]+j,curr[0],curr[1])
                                self.open.append([curr[0]+i,curr[1]+j])
                                self.paintOpen(curr[0]+i,curr[1]+j)
                self.closed[curr[0]-1][curr[1]-1]=True
                if curr[0]!=source.x or curr[1]!=source.y:
                    self.paintClosed(curr[0],curr[1])
        if not(self.isComplete):
            self.con.enableButtons()
            return('No path found')
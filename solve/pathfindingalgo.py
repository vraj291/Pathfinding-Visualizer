import sys
sys.path.insert(1,'d:/python samples/')
from pathfinding_visualizer.node import Node
import time

class BaseAlgo:

    def __init__(self,canvas,con):
        self.bre=37
        self.leng=57
        self.size=20
        self.grid=[[None for x in range(self.bre)] for y in range(self.leng)]
        self.closed=[[False for x in range(self.bre)] for y in range(self.leng)]
        for i in range(1,self.leng+1):
            for j in range(1,self.bre+1):
                self.grid[i-1][j-1]=Node(i,j)
        self.can=canvas
        self.delay=0.01
        self.con=con
        self.diag=False
        self.showSteps=False
        self.pathlist=[]

    def setDimensions(self,l,b):
        self.leng=l
        self.bre=b

    def setComplete(self):
        self.isComplete=True

    def setSize(self,s):
        self.size=s

    def isValid(self,x,y):
        return 0<x<self.leng+1 and 0<y<self.bre+1

    def isBlocked(self,x,y):
        return self.grid[x-1][y-1].isBlock
        
    def isClosed(self,x,y):
        return self.closed[x-1][y-1]
    
    def getParents(self,x,y):
        return [self.grid[x-1][y-1].parent_x,self.grid[x-1][y-1].parent_y]

    def setParents(self,x,y,par_x,par_y):
        self.grid[x-1][y-1].parent_x=par_x
        self.grid[x-1][y-1].parent_y=par_y

    def paintOpen(self,x,y):
        self.can.create_rectangle(x*self.size, y*self.size, (x+1)*self.size, (y+1)*self.size,fill='yellow')
        if self.showSteps:
            time.sleep(self.delay)
            self.can.update()
    
    def paintClosed(self,x,y):
        self.can.create_rectangle(x*self.size, y*self.size, (x+1)*self.size, (y+1)*self.size,fill='green')
        if self.showSteps:
            time.sleep(self.delay)
            self.can.update()
    
    def paintPath(self):
        colors={'violetred4':0,'violet red':0,'medium orchid':0,'purple2':0,'blue violet':0,'dark violet':0,'RoyalBlue3':0}
        excess=len(self.pathlist)%len(colors)
        partitionlen=len(self.pathlist)//len(colors)
        for key in colors:
            if excess>0:
                colors[key]=partitionlen+1
                excess-=1
            else:
                colors[key]=partitionlen
        point=len(self.pathlist)-1
        for key,val in colors.items():
            while(val>0):
                x=self.pathlist[point][0]
                y=self.pathlist[point][1]
                self.can.create_rectangle(x*self.size, y*self.size, (x+1)*self.size, (y+1)*self.size,fill=key)
                val-=1
                point-=1

    def checkSuccessors(self,i,j):
        return (i!=0 or j!=0) and not((i==-1 or i==1) and j!=0) 
    
    def checkSuccessorsDiagonally(self,i,j):
        return (i!=0 or j!=0)

    def setSpeed(self,delay):
        if delay==0:
            delay=1 
        self.delay=0.5/delay

    def setDiagonalPath(self):
        self.diag=True

    def setShowSteps(self):
        self.showSteps=True

    def precheck(self,source,dest):
        if source is None: 
            return [False,'Source not defined.']
        if self.isBlocked(source.x,source.y):
            return [False,'Source is blocked.']
        if dest is None: 
            return [False,'Destination not defined.']
        if self.isBlocked(dest.x,dest.y):
            return [False,'Destination is blocked.']
        return [True,'']

    def tracepath(self,source,dest):
        x=dest.parent_x
        y=dest.parent_y
        while x!=source.x or y!=source.y :
            self.pathlist.append([x,y])
            x,y=self.getParents(x,y)
        self.paintPath()
        
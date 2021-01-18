from math import floor
from tkinter import Frame,Label
import sys,time
sys.path.insert(1,'d:/python samples/')
from pathfinding_visualizer.node import Node

class BaseFrame:

    def __init__(self,frame,canvas,algo):
        self.samp=frame
        self.can=canvas
        self.bre=37
        self.leng=57
        self.size=20
        self.source=None
        self.dest=None
        self.printresult=Label(self.samp,text='')
        self.printresult.place(x=1210,y=400)
        self.graph=algo
        self.bindEvents()
            
    def bindEvents(self):
        self.samp.bind('<Double-Button-1>',self.setSource)
        self.samp.bind('<Double-Button-3>',self.setDest)
        self.samp.bind('<Return>',self.path) 
        self.samp.bind('<Button-3>',self.undo)
        self.samp.bind('<B3-Motion>',self.undo)

    def setDimensions(self,l,b):
        self.leng=l
        self.bre=b
        self.graph.setDimensions(l,b)

    def setSize(self,s):
        self.size=s
        self.graph.setSize(s)

    def isValid(self,x,y):
        return 0<x<self.leng+1 and 0<y<self.bre+1

    def setSource(self,event):
        x=floor(event.x/self.size)
        y=floor(event.y/self.size)
        if self.isValid(x,y):
            if self.source is None :
                self.can.create_rectangle(x*self.size, y*self.size, (x+1)*self.size, (y+1)*self.size,fill='red')
                self.source=Node(x,y)
                self.graph.grid[x-1][y-1].isBlock=False

    def setDest(self,event):
        x=floor(event.x/self.size)
        y=floor(event.y/self.size)
        if self.isValid(x,y):
            if self.dest is None:
                self.can.create_rectangle(x*self.size,y*self.size, (x+1)*self.size, (y+1)*self.size,fill='blue')
                self.dest=Node(x,y)                

    def undo(self,event):
        x=floor(event.x/self.size)
        y=floor(event.y/self.size)
        if self.isValid(x,y):
            self.can.create_rectangle(x*self.size, y*self.size, (x+1)*self.size, (y+1)*self.size, fill='white')
            if self.source is not None and x==self.source.x and y==self.source.y :
                self.source=None
            elif self.dest is not None and x==self.dest.x and y==self.dest.y :
                self.dest=None
            else:
                self.graph.grid[x-1][y-1].isBlock=False

    def path(self,event):
        if self.source is None or self.dest is None:
            self.printresult.config(text='Source or destination is not defined.')
            self.graph.con.enableButtons()
            return
        self.graph.resetBoard(self.source,self.dest)
        start=time.time()
        result=self.graph.findpath(self.source,self.dest)
        end=time.time()
        if result=='Path Found':
            result+=' in '+str(end-start)[:6]+' s'
        self.printresult.config(text=result)
        
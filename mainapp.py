from tkinter import Tk,Canvas,Label,BOTH
import time
import sys 
sys.path.insert(1,'d:/python samples/')
from pathfinding_visualizer.solve.pathfindingalgo import BaseAlgo
from pathfinding_visualizer.solve.djikstras import djikstraspath
from pathfinding_visualizer.solve.astar import Astarpathfinding
from pathfinding_visualizer.node import Node
from pathfinding_visualizer.generate.baseframe import BaseFrame
from pathfinding_visualizer.generate.maze.recursivebacktrackingmaze import RecursiveBacktracking
from pathfinding_visualizer.generate.maze.kruskalsmaze import KruskalsAlgo
from pathfinding_visualizer.generate.userframe import GridFrame
from pathfinding_visualizer.generate.controlhandler import Controller

class Mainframe:

    def __init__(self):
        self.frame=Tk()
        self.frame.geometry('1520x790')
        self.frame.title('Pathfinding Visualizer')
        self.canvas=Canvas(self.frame)
        self.leng=57
        self.bre=37
        self.size=20
        self.createGrid()
        self.createControlPanel()
        self.graph=BaseAlgo(self.canvas,self.con)
        self.grid=BaseFrame(self.frame,self.canvas,self.graph)
        self.frame.bind('<Up>',self.assignNodes)
        self.frame.mainloop()
    
    def createGrid(self):
        for i in range(1,self.leng+1):
            for j in range(1,self.bre+1):
                self.canvas.create_rectangle(i*self.size, j*self.size, (i+1)*self.size, (j+1)*self.size,fill='white')
        self.canvas.pack(fill=BOTH,expand=1)

    def createControlPanel(self):
        self.con=Controller(self.frame)

    def assignNodes(self,event):
        self.createGrid()
        self.grid.printresult.config(text='')
        if self.con.choices['algo']==1:
            self.graph=djikstraspath(self.canvas,self.con)
        else:
            self.graph=Astarpathfinding(self.canvas,self.con)
        if self.con.choices['diagonal']:
            self.graph.setDiagonalPath()
        if self.con.choices['showsteps']:
            self.graph.setShowSteps()
        self.graph.setSpeed(self.con.choices['speed'])
        if self.con.choices['gridcreate']==1:
            self.grid=GridFrame(self.frame,self.canvas,self.graph)
        elif self.con.choices['gridcreate']==2:
            self.grid=RecursiveBacktracking(self.frame,self.canvas,self.graph)
        elif self.con.choices['gridcreate']==3:
            self.grid=KruskalsAlgo(self.frame,self.canvas,self.graph)

if __name__=='__main__':
    obj=Mainframe()


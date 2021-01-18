from math import floor
import sys
import pyautogui
sys.path.insert(0,'d:/python samples/')
from pathfinding_visualizer.generate.baseframe import BaseFrame

class GridFrame(BaseFrame):

    def __init__(self,frame,canvas,algo):
        BaseFrame.__init__(self,frame,canvas,algo)
        self.bindWalls()
    
    def setWalls(self,event):
        abs_coord_x = self.samp.winfo_pointerx() - self.samp.winfo_rootx()
        abs_coord_y = self.samp.winfo_pointery() - self.samp.winfo_rooty()
        x=floor(abs_coord_x/self.size)
        y=floor(abs_coord_y/self.size)
        if self.isValid(x,y):
            if ((self.source is None) or (x!=self.source.x or y!=self.source.y)) and ((self.dest is None) or (x!=self.dest.x or y!=self.dest.y)):
                self.graph.grid[x-1][y-1].isBlock=True
                self.can.create_rectangle(x*self.size, y*self.size, (x+1)*self.size, (y+1)*self.size,fill='grey')

    def bindWalls(self):
        self.samp.bind('<Button-1>',self.setWalls)
        self.samp.bind('<B1-Motion>',self.setWalls)

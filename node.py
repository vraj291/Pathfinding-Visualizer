import math

class Node:
    def __init__(self,xcoor,ycoor):
        self.x=xcoor
        self.y=ycoor
        self.d=math.inf
        self.f=0
        self.h=0
        self.g=0
        self.parent_x=0
        self.parent_y=0
        self.isBlock=False



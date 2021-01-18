import tkinter as tk
from tkinter import Tk,ttk,Button,Scale,Label,Entry,HORIZONTAL,Checkbutton,DISABLED,NORMAL
import pyautogui

class Controller:

    def __init__(self,frame):
        self.frame=frame
        self.choices=None
        self.addControls()
    
    def addControls(self):
        Label(self.frame,text='Controls',font=("Bold", 15)).place(x=1300,y=30)
        Label(self.frame,text='Speed :',font=("Courier", 12)).place(x=1200,y=75)
        self.speed=Scale(self.frame,from_=0,to=100,orient=HORIZONTAL)
        self.speed.place(x=1300,y=60)
        self.speed.set(50)
        self.showSteps=tk.IntVar()
        Label(self.frame,text='Show Steps :',font=("Courier", 12)).place(x=1200,y=115)
        checkSteps=Checkbutton(self.frame,variable=self.showSteps)
        checkSteps.place(x=1350,y=115)
        self.isDiag=tk.IntVar()
        Label(self.frame,text='Diagonal :',font=("Courier", 12)).place(x=1200,y=155)
        checkDiag=Checkbutton(self.frame,variable=self.isDiag)
        checkDiag.place(x=1330,y=155)
        Label(self.frame,text='Algorithm :',font=("Courier", 12)).place(x=1200,y=195)
        self.algochoice = tk.StringVar() 
        algo=ttk.Combobox(self.frame,width=17, textvariable = self.algochoice, values=("Djikstra's Algorithm","A* Search Algorithm"))
        algo.place(x=1350,y=195)
        algo.current(0)
        Label(self.frame,text='Grid :',font=("Courier", 12)).place(x=1200,y=235)
        self.framechoice = tk.StringVar() 
        framec=ttk.Combobox(self.frame, width=23, textvariable = self.framechoice, values=("Manual","Recursive Backtracting Maze","Kruskal's Algorithm Maze"))
        framec.place(x=1280,y=235)
        framec.current(0)
        self.gen=Button(self.frame,text='Generate',width=8,command=self.process)
        self.gen.place(x=1260,y=320)
        self.start=Button(self.frame,text='Start',width=7,command=self.startUp)
        self.start.place(x=1370,y=320)
        self.err=Label(self.frame,text='',font=('Italic',9))
        self.err.place(x=1165,y=400)

    def process(self):
        self.err.config(text='')
        self.choices={'speed':50,'showsteps':False,'diagonal':False,'algo':1,'gridcreate':1} 
        self.choices['speed']=self.speed.get()
        if self.showSteps.get() == 1:
            self.choices['showsteps']= True
        if self.isDiag.get() == 1:
            self.choices['diagonal']= True
        if self.algochoice.get() == "A* Search Algorithm":
            self.choices['algo']=2
        elif self.algochoice.get() != "Djikstra's Algorithm":
            self.err.config(text='An invalid value was entered as algorithm choice.')
            return
        if self.framechoice.get() == 'Recursive Backtracting Maze':
            self.choices['gridcreate']=2
        elif self.framechoice.get() == "Kruskal's Algorithm Maze":
            self.choices['gridcreate']=3
        elif self.framechoice.get() != "Manual":
            self.err.config(text='An invalid value was entered as grid selection choice.')
            return
        pyautogui.press('up')
        
    def startUp(self):
        self.disableButtons()
        pyautogui.press('enter')
        self.isWorking=True

    def disableButtons(self):
        self.start['state']=DISABLED
        self.gen['state']=DISABLED

    def enableButtons(self):
        self.start['state']=NORMAL
        self.gen['state']=NORMAL


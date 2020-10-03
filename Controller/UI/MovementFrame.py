from tkinter import *
import tkinter as tk
from UI.TriangleButton import *

class MovementFrame(tk.LabelFrame):
    def __init__(self, master):
        super(MovementFrame, self).__init__(master, width=235, height=145, text="Tank Movement", font=("Helvetica", 14))
        self.movementComms = None

        self._job = None
        self.root = master

        movementLabelFrame = LabelFrame(self, width = 200, height = 200, borderwidth=0)

        upButton = TriangleButton(movementLabelFrame, 'up')
        downButton = TriangleButton(movementLabelFrame, 'down')
        leftButton = TriangleButton(movementLabelFrame, 'left')
        rightButton = TriangleButton(movementLabelFrame, 'right')
        movementLabelFrame.grid_propagate('false')
        movementLabelFrame.pack_propagate(0)
            
        movementLabelFrame.columnconfigure(0, weight=1)
        movementLabelFrame.columnconfigure(1, weight=1)
        movementLabelFrame.columnconfigure(2, weight=1)

        movementLabelFrame.rowconfigure(0, weight=1)
        movementLabelFrame.rowconfigure(1, weight=1)
        movementLabelFrame.rowconfigure(2, weight=1)

        upButton.grid(row = 0, column = 1, sticky=NSEW)
        downButton.grid(row = 2, column = 1, sticky=NSEW)
        leftButton.grid(row = 1, column = 0, sticky=NSEW)
        rightButton.grid(row =1, column = 2, sticky=NSEW)
        
        speedLabelFrame = LabelFrame(self, borderwidth=0, padx = 0, pady= 0)
        self.SpeedLabel = Label(speedLabelFrame, text= "Speed", font=("Helvetica", 14))
        self.SpeedLabel.pack(side=TOP, fill=BOTH)
        
        self.slider = Scale(speedLabelFrame, from_=100, to=0, width=40, command=self.setSpeed)
        self.slider.pack(side=BOTTOM, fill=Y, expand=True, anchor = CENTER)
        self.slider.set(50)

        movementLabelFrame.pack(side=LEFT, expand=True)
        speedLabelFrame.pack(side=RIGHT, fill=BOTH, expand=True)

        upButton.bind('<ButtonPress-1>',self.upButton)
        upButton.bind('<ButtonRelease-1>',self.stop_motor)

        downButton.bind('<ButtonPress-1>',self.downButton)
        downButton.bind('<ButtonRelease-1>',self.stop_motor)

        leftButton.bind('<ButtonPress-1>',self.leftButton)
        leftButton.bind('<ButtonRelease-1>',self.stop_motor)

        rightButton.bind('<ButtonPress-1>',self.rightButton)
        rightButton.bind('<ButtonRelease-1>',self.stop_motor)

        self.bind('<Configure>', self._on_resize)

    def SetMovement(self, movementComms):
        self.movementComms = movementComms

    def _on_resize(self, event):
        if self.movementComms is not None:
            self.config(width=event.width, height=event.height)

    def upButton(self, t):
        if self.movementComms is not None:
            self.movementComms.MoveForward()
    
    def downButton(self, t):
        if self.movementComms is not None:
            self.movementComms.MoveBackwards()

    def leftButton(self, t):
        if self.movementComms is not None:
            self.movementComms.MoveLeft()

    def rightButton(self, t):
        if self.movementComms is not None:
            self.movementComms.MoveRight()

    def stop_motor(self, t):
        if self.movementComms is not None:
            self.movementComms.MoveStop()

    def setSpeed(self, event):
        if self._job:
            self.root.after_cancel(self._job)

        self._job = self.root.after(500, self.sendNewSpeed)

    def sendNewSpeed(self):
        value = self.slider.get()

        if self.movementComms is not None:
            self.movementComms.SetSpeed(value)
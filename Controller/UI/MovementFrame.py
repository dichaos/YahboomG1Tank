from tkinter import *
import tkinter as tk
from UI.TriangleButton import *

class MovementFrame(tk.LabelFrame):
    def __init__(self, master, width, height, text):
        super(MovementFrame, self).__init__(master, width = width, height = height, text = text)
        self.movementComms = None

        self._job = None
        self.root = master

        labelForm = LabelFrame(self, width = 150, height = 150)

        upButton = TriangleButton(labelForm, 'up')
        downButton = TriangleButton(labelForm, 'down')
        leftButton = TriangleButton(labelForm, 'left')
        rightButton = TriangleButton(labelForm, 'right')
        labelForm.grid_propagate('false')
        labelForm.pack_propagate(0)

        labelForm.columnconfigure(0, weight=1)
        labelForm.columnconfigure(1, weight=1)
        labelForm.columnconfigure(2, weight=1)

        labelForm.rowconfigure(0, weight=1)
        labelForm.rowconfigure(1, weight=1)
        labelForm.rowconfigure(2, weight=1)

        upButton.grid(row = 0, column = 1, sticky=NSEW)
        downButton.grid(row = 2, column = 1, sticky=NSEW)
        leftButton.grid(row = 1, column = 0, sticky=NSEW)
        rightButton.grid(row =1, column = 2, sticky=NSEW)


        
        speedLabelFrame = LabelFrame(self, width = 50, height = 160)
        self.SpeedLabel = Label(speedLabelFrame, text= "Speed")
        self.SpeedLabel.grid(row = 0, column = 0, sticky = NSEW)

        #self.slider = Scale(speedLabelFrame, from_=100, to=0)
        self.slider = Scale(speedLabelFrame, from_=100, to=0, command=self.setSpeed)
        self.slider.grid(row = 1, column = 0, columnspan=2, sticky = NSEW)
        self.slider.set(50)

        labelForm.pack(side=LEFT, fill=BOTH, expand=True)
        speedLabelFrame.pack(side=LEFT, fill=BOTH, expand=True)

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
        print(event)

        if self._job:
            self.root.after_cancel(self._job)

        self._job = self.root.after(500, self.sendNewSpeed)

    def sendNewSpeed(self):
        value = self.slider.get()
        print(value)
        if self.movementComms is not None:
            self.movementComms.SetSpeed(value)
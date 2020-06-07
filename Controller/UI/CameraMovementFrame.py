from tkinter import *
import tkinter as tk
from UI.TriangleButton import *

class CameraMovementFrame(tk.LabelFrame):
    def __init__(self, master, width, height, text, movementComms):
        super(CameraMovementFrame, self).__init__(master, width = width, height = height, text = text)
        self.movementComms = movementComms

        upButton = TriangleButton(self, 'up')
        downButton = TriangleButton(self, 'down')
        leftButton = TriangleButton(self, 'left')
        rightButton = TriangleButton(self, 'right')
        self.grid_propagate('false')
        self.pack_propagate(0)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        upButton.grid(row = 0, column = 1, sticky=NSEW)
        downButton.grid(row = 2, column = 1, sticky=NSEW)
        leftButton.grid(row = 1, column = 0, sticky=NSEW)
        rightButton.grid(row =1, column = 2, sticky=NSEW)

        upButton.bind('<ButtonPress-1>',self.upButton)
        upButton.bind('<ButtonRelease-1>',self.stop_motor)

        downButton.bind('<ButtonPress-1>',self.downButton)
        downButton.bind('<ButtonRelease-1>',self.stop_motor)

        leftButton.bind('<ButtonPress-1>',self.leftButton)
        leftButton.bind('<ButtonRelease-1>',self.stop_motor)

        rightButton.bind('<ButtonPress-1>',self.rightButton)
        rightButton.bind('<ButtonRelease-1>',self.stop_motor)

        self.bind('<Configure>', self._on_resize)

    def _on_resize(self, event):
        self.config(width=event.width, height=event.height)

    def upButton(self, t):
        self.movementComms.CameraUp()
    
    def downButton(self, t):
        self.movementComms.CameraDown()

    def leftButton(self, t):
        self.movementComms.CameraLeft()

    def rightButton(self, t):
        self.movementComms.CameraRight()

    def stop_motor(self, t):
        self.movementComms.CameraUpDownStop()
        self.movementComms.CameraLeftRightStop()
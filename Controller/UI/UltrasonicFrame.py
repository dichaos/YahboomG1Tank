from tkinter import *
import tkinter as tk
from UI.TriangleButton import *

class UltrasonicFrame(tk.LabelFrame):
    def __init__(self, master, width, height, text):
        super(UltrasonicFrame, self).__init__(master, width = width, height = height, text = text, bg="green")
        
        leftButton = TriangleButton(self, 'left')
        rightButton = TriangleButton(self, 'right')

        self.grid_propagate('false')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=1)

        leftButton.grid(row = 0, column = 0, sticky=NSEW)
        rightButton.grid(row = 0, column = 1, sticky = NSEW)

        leftButton.bind('<ButtonPress-1>',self.leftButton)
        leftButton.bind('<ButtonRelease-1>',self.stop_motor)

        rightButton.bind('<ButtonPress-1>',self.rightButton)
        rightButton.bind('<ButtonRelease-1>',self.stop_motor)

        self.bind('<Configure>', self._on_resize)

    def _on_resize(self, event):
        self.config(width=event.width, height=event.height)

    def leftButton(self):
        self.left_callback(self)

    def rightButton(self):
        self.right_callback(self)

    def stop_motor(self, t):
        self.stop_callback(self)

    def left_Button_callback(self, left):
        self.left_callback = left

    def right_Button_callback(self, right):
        self.right_callback = right

    def motor_stop_callback(self, stop):
        self.stop_callback = stop
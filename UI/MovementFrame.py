from tkinter import *
import tkinter as tk
from UI.TriangleButton import *

class MovementFrame(tk.LabelFrame):
    def __init__(self, master, width, height, text):
        super(MovementFrame, self).__init__(master, width = width, height = height, text = text)
        
        upButton = TriangleButton(self, 20,30, 'up', )
        downButton = TriangleButton(self, 20,30, 'down', command = self.downButton)
        leftButton = TriangleButton(self, 30, 20, 'left', command = self.leftButton)
        rightButton = TriangleButton(self, 30, 20, 'right', command = self.rightButton)
        
        upButton.place(x = 50, y = 4)
        downButton.place(x = 50, y = 74)
        leftButton.place(x = 8, y = 44)
        rightButton.place(x = 82, y = 44)

        upButton.bind('<ButtonPress-1>',self.upButton)
        upButton.bind('<ButtonRelease-1>',self.stop_motor)


    def upButton(self, t):
        self.up_callback(self)
    
    def downButton(self):
        self.down_callback(self)

    def leftButton(self):
        self.left_callback(self)

    def rightButton(self):
        self.right_callback(self)

    def stop_motor(self, t):
        self.stop_callback(self)

    def up_Button_callback(self, forward):
        self.up_callback = forward

    def down_Button_callback(self, backward):
        self.down_callback = backward

    def left_Button_callback(self, left):
        self.left_callback = left

    def right_Button_callback(self, right):
        self.right_callback = right

    def motor_stop_callback(self, stop):
        self.stop_callback = stop
from tkinter import *
import tkinter as tk

class TriangleButton(tk.Canvas):
    def __init__(self, master, direction, color='gray', command=None):
        tk.Canvas.__init__(self, master, borderwidth=1,  relief="raised", highlightthickness=0)
        self.command = command
        self.width = 10
        self.height = 10
        self.direction = direction
        self.color = color
        
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.bind('<Configure>', self._on_resize)
        self.draw()

    def draw(self):
        self.delete('all')

        if self.direction == 'down':
            self.create_polygon([0,0, self.width, 0 , (self.width/2), self.height], outline=self.color, fill=self.color, width=2)
        elif self.direction == 'up':
            self.create_polygon([(self.width/2),0,0,self.height,self.width,self.height], outline=self.color, fill=self.color, width=2)
        elif self.direction == 'left':
            self.create_polygon([0, (self.height/2), self.width, 0, self.width, self.height], outline=self.color, fill=self.color, width=2)
        elif self.direction == 'right':
            self.create_polygon([0, 0, self.width, (self.height/2), 0, self.height], outline=self.color, fill=self.color, width=2)

        self.configure(width=self.width, height=self.height)  


    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()

    def _on_resize(self, event):
        self.width = event.width
        self.height = event.height
        self.draw()
        self.config(width=event.width, height=event.height)

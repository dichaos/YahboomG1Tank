from tkinter import *
import tkinter as tk

class TriangleButton(tk.Canvas):
    def __init__(self, parent, width, height, direction, color='gray', command=None):
        tk.Canvas.__init__(self, parent, borderwidth=1,  relief="raised", highlightthickness=0)
        self.command = command

        padding = 4

        if direction == 'down':
            self.create_polygon([padding,padding, width+padding, padding , (width/2) + padding , height+padding], outline=color, fill=color, width=2)
        elif direction == 'up':
            self.create_polygon([(width/2)+padding,padding,padding,height+padding,width+padding,height+padding], outline=color, fill=color, width=2)
        elif direction == 'left':
            self.create_polygon([padding, (height/2)+ padding, width+padding, padding, width+padding, height+padding], outline=color, fill=color, width=2)
        elif direction == 'right':
            self.create_polygon([padding, padding, width+padding, (height/2)+padding, padding, height+padding], outline=color, fill=color, width=2)

        #self.pack()
        (x0,y0,x1,y1)  = self.bbox("all")
        width = (x1-x0) + padding
        height = (y1-y0) + padding
        self.configure(width=width, height=height)  
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()

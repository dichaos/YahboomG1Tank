from tkinter import *
import tkinter as tk
from UI.TriangleButton import *

class TrackSensorFrame(tk.LabelFrame):
    def __init__(self, master):
        super(TrackSensorFrame, self).__init__(master,  height = 75, text = "Tracking Sensor", font=("Helvetica", 14))

        self.grid_propagate('false')
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.First = Label(self, text= "1", borderwidth=2, relief="groove", font=("Helvetica", 14), height=2)
        self.Second = Label(self, text= "2", borderwidth=2, relief="groove", font=("Helvetica", 14))
        self.Third = Label(self, text= "3", borderwidth=2, relief="groove", font=("Helvetica", 14))
        self.Fourth = Label(self, text= "4", borderwidth=2, relief="groove", font=("Helvetica", 14))

        self.First.grid(row = 0, column = 0, sticky = NSEW)
        self.Second.grid(row = 0, column = 1, sticky = NSEW)
        self.Third.grid(row = 0, column = 2, sticky = NSEW)
        self.Fourth.grid(row = 0, column = 3, sticky = NSEW)

    def trackValue(self, t):
        if t[0] == '0':
            self.First.config(bg="black")
            self.First.config(fg="white")
        else:
            self.First.config(bg="white")
            self.First.config(fg="black")

        if t[1] == '0':
            self.Second.config(bg="black")
            self.Second.config(fg="white")
        else:
            self.Second.config(bg="white")
            self.Second.config(fg="black")

        if t[2] == '0':
            self.Third.config(bg="black")
            self.Third.config(fg="white")
        else:
            self.Third.config(bg="white")
            self.Third.config(fg="black")

        if t[3] == '0':
            self.Fourth.config(bg="black")
            self.Fourth.config(fg="white")
        else:
            self.Fourth.config(bg="white")
            self.Fourth.config(fg="black")

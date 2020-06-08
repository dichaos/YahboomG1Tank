from tkinter import *
import tkinter as tk

class LedColorFrame(tk.LabelFrame):
    def __init__(self, master, width, height, text, movementComms):
        super(LedColorFrame, self).__init__(master, width = width, height = height, text = text)

        self.movementComms = movementComms
        self._job = None
        self.root = master

        self.Color = Label(self, text= "", borderwidth=2, relief="groove")
        self.Red = Label(self, text= "", borderwidth=2, relief="groove")
        self.Green = Label(self, text= "", borderwidth=2, relief="groove")
        self.Blue = Label(self, text= "", borderwidth=2, relief="groove")
        
        self.R = Scale(self, from_=255, to=0, command=self.SetColor)
        self.G = Scale(self, from_=255, to=0, command=self.SetColor)
        self.B = Scale(self, from_=255, to=0, command=self.SetColor)
        
        self.Color.grid(row = 0, column = 0, columnspan = 3, sticky = NSEW)
        self.Red.grid(row = 1, column = 0, sticky= NSEW)
        self.Green.grid(row = 1, column = 1, sticky= NSEW)
        self.Blue.grid(row = 1, column = 2, sticky= NSEW)
        self.R.grid(row = 2, column = 0, sticky = NSEW)
        self.G.grid(row = 2, column = 1, sticky = NSEW)
        self.B.grid(row = 2, column = 2, sticky = NSEW)

    def SetColor(self, event):
        if self._job:
            self.root.after_cancel(self._job)

        self.Color.config(bg="#{:02x}{:02x}{:02x}".format(self.R.get(), self.G.get(), self.B.get()))
        self.Red.config(bg="#{:02x}{:02x}{:02x}".format(self.R.get(), 0, 0))
        self.Green.config(bg="#{:02x}{:02x}{:02x}".format(0, self.G.get(), 0))
        self.Blue.config(bg="#{:02x}{:02x}{:02x}".format(0, 0, self.B.get()))

        self._job = self.root.after(500, self.SendColor)

    def SendColor(self):
        self.movementComms.SendColor(self.R.get(), self.G.get(), self.B.get())


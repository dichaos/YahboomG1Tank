from tkinter import *
import tkinter as tk

class LedColorFrame(tk.LabelFrame):
    def __init__(self, master):
        super(LedColorFrame, self).__init__(master, text = "Headlights",  font=("Helvetica", 14))
        self.movementComms = None
        self._job = None
        self.root = master

        self.Color = Label(self, text= "", borderwidth=2, relief="groove", height=2)
        self.Red = Label(self, text= "", borderwidth=2, relief="groove", height=2)
        self.Green = Label(self, text= "", borderwidth=2, relief="groove", height=2)
        self.Blue = Label(self, text= "", borderwidth=2, relief="groove", height=2)
        
        self.R = Scale(self, from_=255, to=0, width=35, command=self.SetColor,  font=("Helvetica", 8))
        self.G = Scale(self, from_=255, to=0, width=35, command=self.SetColor,  font=("Helvetica", 8))
        self.B = Scale(self, from_=255, to=0, width=35, command=self.SetColor,  font=("Helvetica", 8))
        
        self.Color.grid(row = 0, column = 0, columnspan = 3, sticky = NSEW)
        self.Red.grid(row = 1, column = 0, sticky= NSEW)
        self.Green.grid(row = 1, column = 1, sticky= NSEW)
        self.Blue.grid(row = 1, column = 2, sticky= NSEW)

        self.R.grid(row = 2, column = 0, sticky = NW)
        self.G.grid(row = 2, column = 1, sticky = NW)
        self.B.grid(row = 2, column = 2, sticky = NW)

        self.turnOffButton = Button(self,  text = 'Turn Off', height= 1, font=("Helvetica", 14), command=self.TurnOff)
        self.turnOffButton.grid(row = 3, column = 0, columnspan=3, sticky=NSEW)
    
    def SetMovement(self, movementComms):
        self.movementComms = movementComms

    def TurnOff(self):
        self.R.set(0)
        self.G.set(0)
        self.B.set(0)
        self.SetColor(None)


    def SetColor(self, event):
        self.Color.config(bg="#{:02x}{:02x}{:02x}".format(self.R.get(), self.G.get(), self.B.get()))
        self.Red.config(bg="#{:02x}{:02x}{:02x}".format(self.R.get(), 0, 0))
        self.Green.config(bg="#{:02x}{:02x}{:02x}".format(0, self.G.get(), 0))
        self.Blue.config(bg="#{:02x}{:02x}{:02x}".format(0, 0, self.B.get()))
        
        if self._job:
            self.root.after_cancel(self._job)

        self._job = self.root.after(500, self.SendColor)

    def SendColor(self):
        if self.movementComms is not None: 
            self.movementComms.SendColor(self.R.get(), self.G.get(), self.B.get())
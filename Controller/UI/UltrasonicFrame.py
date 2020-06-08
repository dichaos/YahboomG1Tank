from tkinter import *
import tkinter as tk
from UI.TriangleButton import *

class UltrasonicFrame(tk.LabelFrame):
    def __init__(self, master, width, height, text, movementComms):
        super(UltrasonicFrame, self).__init__(master, width = width, height = height, text = text)
        self.movementComms = movementComms

        self._job = None
        self.root = master

        self.grid_propagate('false')
        self.grid_columnconfigure(0, weight=1)

        self.slider = Scale(self, from_=2500, to=500, orient=HORIZONTAL, command=self.updateValue)
        self.slider.grid(row = 0, column = 0, columnspan=2, sticky = NSEW, ipadx=2, ipady =2)
        self.slider.set(1500)

        self.DistanceLabel = Label(self, text= "Distance : 0 cm")
        self.DistanceLabel.grid(row = 1, column = 0, sticky = NSEW, ipadx=2, ipady =2)

        self.CenterButton = Button(self, text="Center", command=self.center)
        self.CenterButton.grid(row = 1, column = 1, sticky = NSEW, ipadx=2, ipady =2)

        self.bind('<Configure>', self._on_resize)

    def updateValue(self, event):
        if self._job:
            self.root.after_cancel(self._job)

        self._job = self.root.after(500, self.sendUpdateValue)

    def center(self):
        self.slider.set(1500)

    def sendUpdateValue(self):
        value = self.slider.get()
        self.movementComms.UltrsonicSetValue(value)

    def _on_resize(self, event):
        self.config(width=event.width, height=event.height)

    def ultrasonicValue(self, t):
        self.DistanceLabel.configure(text="Distance :"+t+"cm")
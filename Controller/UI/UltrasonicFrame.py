from tkinter import *
import tkinter as tk

class UltrasonicFrame(tk.LabelFrame):
    def __init__(self, master):
        super(UltrasonicFrame, self).__init__(master, width=310, height=120, text="Ultrasonic Sensor",  font=("Helvetica", 14))
        self.movementComms = None
        self._job = None
        self.root = master

        self.grid_propagate('false')
        self.grid_columnconfigure(0, weight=1)

        self.slider = Scale(self, from_=180, to=0, width=35, orient=HORIZONTAL, command=self.updateValue, showvalue='false')
        self.slider.grid(row = 0, column = 0, columnspan=2, sticky = NSEW, ipadx=2, ipady =2)
        self.slider.set(90)

        self.DistanceLabel = Label(self, text= "Distance : 0 cm", font=("Helvetica", 14))
        self.DistanceLabel.grid(row = 1, column = 0, sticky = NSEW, ipadx=2, ipady =2)

        self.CenterButton = Button(self, text="Center", command=self.center, width = 10,  font=("Helvetica", 14))
        self.CenterButton.grid(row = 1, column = 1, sticky = NSEW, ipadx=4, ipady =2)

        self.bind('<Configure>', self._on_resize)

    def SetMovement(self, movementComms):
        self.movementComms = movementComms

    def updateValue(self, event):
        if self._job:
            self.root.after_cancel(self._job)

        self._job = self.root.after(500, self.sendUpdateValue)

    def center(self):
        self.slider.set(90)
        self.sendUpdateValue()

    def sendUpdateValue(self):
        value = self.slider.get()
        
        if self.movementComms is not None:
            self.movementComms.UltrsonicSetValue(value)

    def _on_resize(self, event):
        self.config(width=event.width, height=event.height)

    def ultrasonicValue(self, t):
        self.DistanceLabel.configure(text="Distance :"+t+"cm")
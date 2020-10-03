from tkinter import *
import tkinter as tk

class BuzzerFrame(tk.LabelFrame):
    def __init__(self, master):
        super(BuzzerFrame, self).__init__(master, text = "Buzzer", font=("Helvetica", 14))
        self.movementComms = None
        upButton = Button(self, text='Annoy', font=("Helvetica", 14), width=17)
        upButton.pack(fill=BOTH, expand=True)

        upButton.bind('<ButtonPress-1>',self.BuzzOn)
        upButton.bind('<ButtonRelease-1>',self.BuzzOff)

    def SetMovement(self, movementComms):
        self.movementComms = movementComms

    def BuzzOn(self, event):
        if self.movementComms is not None:
            self.movementComms.BuzzOn()

    def BuzzOff(self, event):
        if self.movementComms is not None:
            self.movementComms.BuzzOff()
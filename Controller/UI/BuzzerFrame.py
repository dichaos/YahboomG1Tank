from tkinter import *
import tkinter as tk

class BuzzerFrame(tk.LabelFrame):
    def __init__(self, master, width, height, text):
        super(BuzzerFrame, self).__init__(master, width = width, height = height, text = text)
        self.movementComms = None
        upButton = Button(self, text='Annoy')
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
from tkinter import *
import tkinter as tk


class ConnectionFrame(tk.LabelFrame):
    def __init__(self, master, width, height, text):
        super(ConnectionFrame, self).__init__(master, width = width, height = height, text = text)

        lb1 = Label(self, text ='IP:')
        lb1.grid(row = 0, column = 0, sticky = E, padx= 3, pady = 3)

        self.IPEntry = Entry(self, width = 15)
        self.IPEntry.grid(row = 0, column = 1, padx= 3, pady = 3)

        connectionButton = Button(self,  text = 'connect', width = 10)
        connectionButton.grid(row = 0, column = 2, padx= 3, pady = 3)
        
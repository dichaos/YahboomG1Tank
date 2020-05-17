from tkinter import *
import tkinter as tk


class ConnectionFrame(tk.LabelFrame):
    def __init__(self, master, width, height, text):
        super(ConnectionFrame, self).__init__(master, width = width, height = height, text = text)
        #self.master = master

        lb1 = Label(self, text ='IP')
        lb1.grid(row = 0, column = 0, sticky = W)

        IPEntry = Entry(self, width = 15)
        IPEntry.grid(row = 0, column = 1)

        connectionButton = Button(self,  text = 'connect')
        connectionButton.grid(row = 0, column = 2)
        
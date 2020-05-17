from tkinter import *
import tkinter
from UI.MovementFrame import *
from UI.ConnectionFrame import *
import os

class MainWindow(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        
        location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.master.iconphoto(False, tk.PhotoImage(file=os.path.join(location, 'robot.png')))
        self.master.title("Yahboom Tank Commander")

        self.pack()

        ConnectionPanel = ConnectionFrame(self, width = 135, height = 5, text = "Connection")
        ConnectionPanel.grid(row = 0, column = 0)

        self.MovementPanel = MovementFrame(self, width=135, height=145, text="Movement")
        self.MovementPanel.grid(row = 1, column = 0, sticky=NW)

    def up_Button_callback(self, forward):
        self.MovementPanel.up_Button_callback(forward)

    def down_Button_callback(self, backward):
        self.MovementPanel.down_Button_callback(backward)

    def left_Button_callback(self, left):
        self.MovementPanel.left_Button_callback(left)

    def right_Button_callback(self, right):
        self.MovementPanel.right_Button_callback(right)

    def motor_stop_callback(self, stop):
        self.MovementPanel.motor_stop_callback(stop)
    
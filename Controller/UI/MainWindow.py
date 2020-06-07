from tkinter import *
import tkinter
from UI.MovementFrame import *
from UI.ConnectionFrame import *
from UI.CameraFrame import *
from UI.UltrasonicFrame import *
import os

class MainWindow(Frame):
    def __init__(self, master, movementComms):
        Frame.__init__(self, master)               
        self.master = master
        
        location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.master.iconphoto(False, tk.PhotoImage(file=os.path.join(location, 'robot.png')))
        self.master.title("Yahboom Tank Commander")
        
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(1, weight = 2)
        self.rowconfigure(2, weight = 2)

        ConnectionPanel = ConnectionFrame(self, width = 135, height = 5, text = "Connection")
        ConnectionPanel.grid(row=0, column =0, columnspan = 2, sticky="nsew")
        
        self.MovementPanel = MovementFrame(self, width=135, height=145, text="Tank Movement", movementComms=movementComms)
        self.MovementPanel.grid(row = 1, column = 0)
        
        self.ultrasonicPanel = UltrasonicFrame(self, width=135, height=145, text="Ultrasonic Sensor")
        self.ultrasonicPanel.grid(row = 1, column =1, sticky = "nw")
        
        self.CameraFrame = CameraFrame(self, 150,150, "Camera", movementComms=movementComms)
        self.CameraFrame.pack_propagate(0)
        self.CameraFrame.grid(row =2, column = 0, columnspan=2, sticky="nsew", padx =5, pady = 5)

    def movement_up_Button_callback(self, forward):
        self.MovementPanel.up_Button_callback(forward)

    def movement_down_Button_callback(self, backward):
        self.MovementPanel.down_Button_callback(backward)

    def movement_left_Button_callback(self, left):
        self.MovementPanel.left_Button_callback(left)

    def movement_right_Button_callback(self, right):
        self.MovementPanel.right_Button_callback(right)

    def movement_motor_stop_callback(self, stop):
        self.MovementPanel.motor_stop_callback(stop)

    def ultrasonic_motor_left_callback(self, left):
        self.ultrasonic_motor_left_callback(left)

    def ultrasonic_motor_right_callback(self, right):
        self.ultrasonic_motor_right_callback(right)

    def newImage(self, image):
        self.CameraFrame.new_image(LastImage=image)
    
    def ultraSonicValue(self, value):
        self.ultrasonicPanel.ultrasonicValue(value)

    def infraredValue(self, value):
        print(value)
from tkinter import *
import tkinter
from UI.MovementFrame import *
from UI.ConnectionFrame import *
from UI.CameraFrame import *
from UI.UltrasonicFrame import *
from UI.TrackSensorFrame import *
from UI.LedColorFrame import *
from UI.BuzzerFrame import *
import os

class MainWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)               
        self.master = master
        
        location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.master.iconphoto(False, tk.PhotoImage(file=os.path.join(location, 'robot.png')))
        self.master.title("Yahboom Tank Commander")
        
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(1, weight = 2)
        #self.rowconfigure(2, weight = 2)

        self.ConnectionPanel = ConnectionFrame(self, width = 135, height = 5, text = "Connection")
        self.ConnectionPanel.grid(row=0, column =0, sticky="nsew")
        
        self.MovementPanel = MovementFrame(self, width=135, height=145, text="Tank Movement")
        self.MovementPanel.grid(row = 1, column = 0)
        
        self.ultrasonicPanel = UltrasonicFrame(self, width=310, height=100, text="Ultrasonic Sensor")
        self.ultrasonicPanel.grid(row = 2, column =0, sticky = "nw")

        self.trackSensorFrame = TrackSensorFrame(self, width=310, height = 45, text = "Tracking Sensor")
        self.trackSensorFrame.grid(row = 3, column = 0, sticky ="nw")

        self.ledColorFrame = LedColorFrame(self, width= 310, height = 200, text = "Headlights")
        self.ledColorFrame.grid(row=4, column=0, sticky ="nw")

        self.BuzzerFrame = BuzzerFrame(self, width=310, height = 50, text = "Buzzer")
        self.BuzzerFrame.grid(row=5, column = 0, sticky = "nw")
        
        self.CameraFrame = CameraFrame(self, 152,150, "Camera")
        self.CameraFrame.pack_propagate(0)
        self.CameraFrame.grid(row =0, column = 1, rowspan=6, sticky="nsew", padx =2, pady = 5)

        self.ConnectionPanel.CreateConnections(self)

    def newImage(self, image):
        self.CameraFrame.new_image(LastImage=image)
    
    def ultraSonicValue(self, value):
        self.ultrasonicPanel.ultrasonicValue(value)

    def TrackValue(self, value):
        self.trackSensorFrame.trackValue(value)
        
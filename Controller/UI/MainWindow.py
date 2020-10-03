from tkinter import *
import tkinter
from UI.MovementFrame import *
from UI.ConnectionFrame import *
from UI.CameraFrame import *
from UI.UltrasonicFrame import *
from UI.TrackSensorFrame import *
from UI.LedColorFrame import *
from UI.BuzzerFrame import *
from UI.RecordVideoFrame import *
import threading
import os

class MainWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)               
        self.master = master
        
        location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.master.iconphoto(False, tk.PhotoImage(file=os.path.join(location, 'robot.png')))
        self.master.title("Yahboom Tank Commander")
        
        self.pack(fill=BOTH)#, expand=1)

        #self.columnconfigure(1, weight = 2)

        self.ConnectionPanel = ConnectionFrame(self)
        self.ConnectionPanel.grid(row=0, column =0, sticky="new",padx=2)
        
        self.MovementPanel = MovementFrame(self)
        self.MovementPanel.grid(row = 1, column = 0, sticky = "new",padx=2)
        
        self.ultrasonicPanel = UltrasonicFrame(self)
        self.ultrasonicPanel.grid(row = 2, column =0, sticky = "new",padx=2)

        self.trackSensorFrame = TrackSensorFrame(self)
        self.trackSensorFrame.grid(row = 3, column = 0, sticky ="new",padx=2)

        self.CameraFrame = CameraFrame(self)
        self.CameraFrame.grid(row =0, column = 1, rowspan=4, sticky="nesw",padx=2)

        self.RecordVideoFrame = RecordVideoFrame(self)
        self.RecordVideoFrame.grid(row=0, column = 2, sticky="nw",padx=2)

        self.ledColorFrame = LedColorFrame(self)
        self.ledColorFrame.grid(row = 1, column = 2, sticky = "nw",padx=2)

        self.BuzzerFrame = BuzzerFrame(self)
        self.BuzzerFrame.grid(row = 3, column = 2, rowspan=2, sticky="nw",padx=2)        

    def newImage(self, image):
        self.CameraFrame.new_image(LastImage=image)
    
    def ultraSonicValue(self, value):
        self.ultrasonicPanel.ultrasonicValue(value)

    def TrackValue(self, value):
        self.trackSensorFrame.trackValue(value)

    def close(self):
        self.ConnectionPanel.Close()

    def ResetValues(self):
        self.ledColorFrame.TurnOff()
        self.CameraFrame.center()
        self.MovementPanel.sendNewSpeed()
        self.BuzzerFrame.BuzzOff(None)
        self.ultrasonicPanel.center()

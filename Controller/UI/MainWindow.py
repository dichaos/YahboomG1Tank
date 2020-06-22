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
        
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(1, weight = 2)

        self.ConnectionPanel = ConnectionFrame(self)
        self.ConnectionPanel.grid(row=0, column =0, sticky="nsew")
        
        self.MovementPanel = MovementFrame(self)
        self.MovementPanel.grid(row = 1, column = 0, sticky = "nsew")
        
        self.ultrasonicPanel = UltrasonicFrame(self)
        self.ultrasonicPanel.grid(row = 2, column =0, sticky = "nw")

        self.trackSensorFrame = TrackSensorFrame(self)
        self.trackSensorFrame.grid(row = 3, column = 0, sticky ="nw")


        smallGroup = LabelFrame(self)
        smallGroup.grid_rowconfigure(0, weight=1)
        smallGroup.grid_columnconfigure(1, weight=1)
        self.ledColorFrame = LedColorFrame(smallGroup)
        self.ledColorFrame.grid(row = 0, column = 0, rowspan=2)


        self.BuzzerFrame = BuzzerFrame(smallGroup)
        self.BuzzerFrame.grid(row = 0, column = 1, sticky="new")

        self.RecordVideoFrame = RecordVideoFrame(smallGroup)
        self.RecordVideoFrame.grid(row=1, column = 1, sticky="new")

        smallGroup.grid(row=4, column=0, sticky= "nsew")
        
        self.CameraFrame = CameraFrame(self)
        self.CameraFrame.grid(row =0, column = 1, rowspan=5, sticky="nsew")

        self.disableChildren(self)
        self.DoTheConnection()

    def newImage(self, image):
        self.CameraFrame.new_image(LastImage=image)
    
    def ultraSonicValue(self, value):
        self.ultrasonicPanel.ultrasonicValue(value)

    def TrackValue(self, value):
        self.trackSensorFrame.trackValue(value)

    def DoTheConnection(self):
        thread = threading.Thread(target=self.Connect)
        thread.daemon = True       
        thread.start() 

    def Connect(self):
        wait = self.wait()
        self.ConnectionPanel.CreateConnections(self)
        wait.destroy()
        self.enableChildren(self)

    def disableChildren(self, parent):
        for child in parent.winfo_children():
            wtype = child.winfo_class()
            if wtype not in ('Frame','Labelframe'):
                try:
                    child.configure(state='disable')
                except:
                    pass
            else:
                self.disableChildren(child)
    
    def enableChildren(self, parent):
        for child in parent.winfo_children():
            wtype = child.winfo_class()
            if wtype not in ('Frame','Labelframe'):
                child.configure(state='normal')
            else:
                self.enableChildren(child)
    
    def wait(self):
        win = Toplevel(self)
        
        win.geometry("800x300+300+300")
        win.overrideredirect(1)
        
        win.lift()
        l = Label(win, text='Wait to connect please...')
        l.config(font=("Courier", 30))
        l.pack(fill="none", expand=True)
        return win
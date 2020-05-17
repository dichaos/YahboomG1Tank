from tkinter import *
import tkinter
from UI.MainWindow import *
from Events.DektopEvents import *
import Events.DektopEvents as de
from Comms import *
import Comms as c

root = Tk()

#create window
root.geometry("400x300")
app = MainWindow(root)

#create comms
socket = c.MySocket()



events = DesktoEvents(None)


#set button events
app.up_Button_callback(events.MoveForward)
app.down_Button_callback(events.MoveBackwards)
app.left_Button_callback(events.MoveLeft)
app.right_Button_callback(events.MoveRight)
app.motor_stop_callback(events.MoveStop)

root.mainloop()


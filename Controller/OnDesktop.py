from tkinter import *
import tkinter
from UI.MainWindow import *
from Events.MovementEvents import *
import Events.MovementEvents as de
from Comms.VideoComms import *
import Comms.VideoComms as c
import Comms.UtrasonicComms as u
import Comms.InfraredComms as i

root = Tk()

#create window
root.geometry("800x600")
root.minsize(800, 600)
app = MainWindow(root)

#create comms
videoStream = c.VideoComms('tcp://*:5555', app)
ultrasonicStream = u.UltrasonicComms('tcp://*:6666', app)
infraredStream = i.InfraredComms('tcp://*:7777', app)

events = MovementEvents(None)

#set button events
app.movement_up_Button_callback(events.MoveForward)
app.movement_down_Button_callback(events.MoveBackwards)
app.movement_left_Button_callback(events.MoveLeft)
app.movement_right_Button_callback(events.MoveRight)
app.movement_motor_stop_callback(events.MoveStop)
   
videoStream.start()
ultrasonicStream.start()
infraredStream.start()

root.mainloop()



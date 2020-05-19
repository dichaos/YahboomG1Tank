from tkinter import *
import tkinter
from UI.MainWindow import *
from Events.MovementEvents import *
import Events.MovementEvents as de
from VideoComms import *
import VideoComms as c
import threading


def start_thread(socket):
    socket.start()

root = Tk()

#create window
root.geometry("800x600")
root.minsize(800, 600)
app = MainWindow(root)

#create comms
socket = c.VideoComms(app)

events = MovementEvents(None)

#set button events
app.movement_up_Button_callback(events.MoveForward)
app.movement_down_Button_callback(events.MoveBackwards)
app.movement_left_Button_callback(events.MoveLeft)
app.movement_right_Button_callback(events.MoveRight)
app.movement_motor_stop_callback(events.MoveStop)


thread = threading.Thread(target=start_thread, args=(socket,))
thread.daemon = True       
thread.start()     

root.mainloop()



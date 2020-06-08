from tkinter import *
import tkinter
from Comms.VideoComms import *
import Comms.VideoComms as c
import Comms.UtrasonicComms as u
import Comms.InfraredComms as i
import Comms.Streamer as s
import Comms.MovementComms as m
import UI.MainWindow as mainWindow

root = Tk()

#create window
root.geometry("1024x600")
root.resizable(False, False)
root.minsize(800, 600)


#create write comms
movementStream = s.Streamer('tcp://*:9999')
movement = m.MovementComms(movementStream)

app = mainWindow.MainWindow(root, movement)

#create read comms
videoStream = c.VideoComms('tcp://*:5555', app)
ultrasonicStream = u.UltrasonicComms('tcp://*:6666', app)
infraredStream = i.InfraredComms('tcp://*:7777', app)

videoStream.start()
ultrasonicStream.start()
infraredStream.start()

root.mainloop()



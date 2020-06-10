from tkinter import *
import tkinter as tk
import Comms.NetworkReader as NetworkReader
from Comms.VideoComms import *
import Comms.VideoComms as c
import Comms.UtrasonicComms as u
import Comms.InfraredComms as i
import Comms.Streamer as s
import Comms.MovementComms as m
import tkinter as tk
import os

class ConnectionFrame(tk.LabelFrame):
    def __init__(self, master):
        super(ConnectionFrame, self).__init__(master, text = "Connection")

        lb1 = Label(self, text ='IP:')
        lb1.grid(row = 0, column = 0, sticky = E, padx= 3, pady = 3)

        self.IPEntry = Entry(self, width = 15)
        self.IPEntry.grid(row = 0, column = 1, padx= 3, pady = 3)

        connectionButton = Button(self,  text = 'Save', width = 10, command=self.Save)
        connectionButton.grid(row = 0, column = 2, padx= 3, pady = 3)

    def Save(self):
        f = open("OnDesktop.config", "r")
        contents = f.readlines()
        f.close()

        contents.insert(0, "IP="+self.IPEntry.get()+" \n")

        f = open("OnDesktop.config", "w")
        contents = "".join(contents)
        f.write(contents)
        f.close()

    def CreateConnections(self, app):

        with open ("OnDesktop.config", "r") as myfile:
            line = myfile.readlines()[0]
            
            if line.startswith("hostname"):
                hostname=line.split("=")[1]
                self.ip = NetworkReader.GetIp(hostname)
            elif line.startswith("IP"):
                self.ip = line.split("=")[1].strip()

        #self.IPEntry.delete(0,"end")
        self.IPEntry.insert(0, self.ip)

        movementStream = s.Streamer('tcp://'+self.ip+':9999')
        movement = m.MovementComms(movementStream)

        app.MovementPanel.SetMovement(movement)
        app.ultrasonicPanel.SetMovement(movement)
        app.ledColorFrame.SetMovement(movement)
        app.CameraFrame.SetMovement(movement)
        app.BuzzerFrame.SetMovement(movement)

        #create read comms
        videoStream = c.VideoComms('tcp://'+self.ip+':5555', app)
        ultrasonicStream = u.UltrasonicComms('tcp://'+self.ip+':6666', app)
        infraredStream = i.InfraredComms('tcp://'+self.ip+':7777', app)

        movementStream.start()
        videoStream.start()
        ultrasonicStream.start()
        infraredStream.start()
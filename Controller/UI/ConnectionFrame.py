from tkinter import *
import tkinter as tk
import Comms.NetworkReader as NetworkReader
import Comms.VideoComms as c
import Comms.UtrasonicComms as u
import Comms.InfraredComms as i
import Comms.MovementComms as m
import Comms.AudioComms as a
import tkinter as tk
import traceback
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
        self.SetIp()

    def Save(self):
        f = open("OnDesktop.config", "r")
        contents = f.readlines()
        f.close()

        contents.insert(0, "IP="+self.IPEntry.get()+" \n")

        f = open("OnDesktop.config", "w")
        contents = "".join(contents)
        f.write(contents)
        f.close()

    def SetIp(self):
        with open ("OnDesktop.config", "r") as myfile:
            line = myfile.readlines()[0]
            
            if line.startswith("hostname"):
                hostname=line.split("=")[1]
                self.ip = NetworkReader.GetIp(hostname)
            elif line.startswith("IP"):
                self.ip = line.split("=")[1].strip()

        self.IPEntry.delete(0,END)
        self.IPEntry.insert(END, self.ip)

    def CreateConnections(self, app):
        self.movement = m.MovementComms(self.ip, 9999)
        self.movement.start()
        
        app.MovementPanel.SetMovement(self.movement)
        app.ultrasonicPanel.SetMovement(self.movement)
        app.ledColorFrame.SetMovement(self.movement)
        app.CameraFrame.SetMovement(self.movement)
        app.BuzzerFrame.SetMovement(self.movement)
        
        #create read comms
        self.ultrasonicStream = u.UltrasonicComms(1000, app)
        self.infraredStream = i.InfraredComms(1001, app)
        self.videoStream = c.VideoComms(1002, app)
        self.audioStream = a.AudioComms(1003)

        self.videoStream.start()
        self.ultrasonicStream.start()
        self.infraredStream.start()
        self.audioStream.start()
        app.RecordVideoFrame.SetAudio(self.audioStream)
        app.RecordVideoFrame.SetVideo(self.videoStream)

    def Close(self):
        try:
            self.ultrasonicStream.stop()
            self.infraredStream.stop()
            self.videoStream.stop()
            self.audioStream.stop()
            self.movement.stop()
        except Exception as e:
            traceback.print_exc()
            print(e)
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
        super(ConnectionFrame, self).__init__(master, text = "Connection", font=("Helvetica", 14))
        self.MainWindow = master
        lb1 = Label(self, text ='IP:', font=("Helvetica", 14))
        lb1.grid(row = 0, column = 0, sticky = E, padx= 3, pady = 3)

        self.IPEntry = Entry(self, width = 14, font=("Helvetica", 14))
        self.IPEntry.grid(row = 0, column = 0, padx= 3, pady = 3)

        connectionButton = Button(self,  text = 'Connect', width = 10, height= 2, font=("Helvetica", 14), command=self.Connect)
        connectionButton.grid(row = 0, column = 1, padx= 3, pady = 3)
        
        self.Connection = Label(self, text= "Disconnected", bg="red", borderwidth=2, relief="groove", font=("Helvetica", 14), height=2)
        self.Connection.grid(row=1, column=0, columnspan=2, sticky= NSEW)

        self.SetIp()

    def Connect(self):
        self.CreateConnections()

    def SetConfig(self):
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

    def CreateConnections(self):
        self.movement = m.MovementComms(self.ip, 9999)

        self.MainWindow.MovementPanel.SetMovement(self.movement)
        self.MainWindow.ultrasonicPanel.SetMovement(self.movement)
        self.MainWindow.ledColorFrame.SetMovement(self.movement)
        self.MainWindow.CameraFrame.SetMovement(self.movement)
        self.MainWindow.BuzzerFrame.SetMovement(self.movement)

        self.ultrasonicStream = u.UltrasonicComms(2000, self.MainWindow)
        self.infraredStream = i.InfraredComms(2001, self.MainWindow)
        self.videoStream = c.VideoComms(2002, self.MainWindow)
        self.audioStream = a.AudioComms(2003)

        con = self.movement.start()
        self.videoStream.start()
        self.audioStream.start()
        self.ultrasonicStream.start()
        self.infraredStream.start()
        
        self.MainWindow.RecordVideoFrame.SetAudio(self.audioStream)
        self.MainWindow.RecordVideoFrame.SetVideo(self.videoStream)

        if con==True:
            print("Connected about to reset robot")
            self.SetConfig()
            self.Connection.config(bg="green", text="Connected")
            self.MainWindow.ResetValues()

    def Close(self):
        try:
            self.movement.stop()
            print("Movement stopped")
            self.videoStream.stop()
            print("Video stopped")
            self.audioStream.stop()
            print("Audio stopped")
            self.ultrasonicStream.stop()
            print("Ultrasonic stopped")
            self.infraredStream.stop()
            print("Infrared stopped")
        except Exception as e:
            traceback.print_exc()
            print(e)
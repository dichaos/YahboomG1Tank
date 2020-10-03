from tkinter import *
import subprocess
import tkinter as tk
import os

class RecordVideoFrame(tk.LabelFrame):
    def __init__(self, master):
        super(RecordVideoFrame, self).__init__(master, text = "Video", font=("Helvetica", 14))
        self.AudioComms = None

        self.muteButton = Button(self, text='Mute', font=("Helvetica", 14), command = self.Mute, width=17, height=3)
        self.muteButton.pack(fill=BOTH, expand=True)

        self.recordButton = Button(self, text='Record', font=("Helvetica", 14), command = self.Record, width=17, height=3)
        self.recordButton.pack(fill=BOTH, expand=True)

        self.mute = 0
        self.recording = 0

    def SetAudio(self, AudioComms):
        self.AudioComms = AudioComms

    def SetVideo(self, VideoComms):
        self.VideoComms = VideoComms

    def Mute(self):
        if self.mute == 0:
            self.AudioComms.stop()
            self.muteButton.configure(relief='sunken')
            self.mute = 1
        elif self.mute == 1:
            self.AudioComms.start()
            self.muteButton.configure(relief='raised')
            self.mute = 0

    def Record(self):
        if self.recording == 0:
            self.AudioComms.Record()
            self.VideoComms.Record()
            self.recordButton.configure(relief='sunken')
            self.recording = 1
        elif self.recording == 1:
            fileName = self.GetFileName()

            self.AudioComms.RecordStop()
            self.VideoComms.RecordStop()
            
            cmd = "ffmpeg -i video.mpeg -i audio.wav -c:v copy -c:a aac "+fileName
            subprocess.call(cmd, shell=True)

            self.recording = 0
            self.DeleteTempFiles()
            self.recordButton.configure(relief='raised')

    def DeleteTempFiles(self):
        if os.path.exists("video.mpeg"):
            os.remove("video.mpeg")

        if os.path.exists("audio.wav"):
            os.remove("audio.wav")

    def GetFileName(self):
        filename = "video.mp4"
        count = 0
        
        while os.path.exists(filename) == True:
            count = count + 1
            filename = "video"+str(count)+".mp4"
        
        return filename
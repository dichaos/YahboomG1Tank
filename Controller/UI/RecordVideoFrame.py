from tkinter import *
import subprocess
import tkinter as tk
import os

class RecordVideoFrame(tk.LabelFrame):
    def __init__(self, master):
        super(RecordVideoFrame, self).__init__(master, text = "Audio")
        self.AudioComms = None

        self.muteButton = Button(self, text='Mute', command = self.Mute)
        self.muteButton.pack(fill=BOTH, expand=True)

        self.recordButton = Button(self, text='Record', command = self.Record)
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
            self.AudioComms.RecordStop()
            self.VideoComms.RecordStop()
            
            os.remove("video.mp4")
            
            cmd = 'ffmpeg -i video.mpeg -i audio.wav -c:v copy -c:a aac video.mp4'
            subprocess.call(cmd, shell=True)
            self.recording = 0

            os.remove("video.mpeg")
            os.remove("audio.wav")

            self.recordButton.configure(relief='raised')
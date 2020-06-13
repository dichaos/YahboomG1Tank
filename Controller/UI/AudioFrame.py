from tkinter import *
import tkinter as tk

class AudioFrame(tk.LabelFrame):
    def __init__(self, master):
        super(AudioFrame, self).__init__(master, text = "Audio")
        self.AudioComms = None

        self.muteButton = Button(self, text='Mute', command = self.Mute)
        self.muteButton.pack(fill=BOTH, expand=True)

        self.recordButton = Button(self, text='Record', command = self.Record)
        self.recordButton.pack(fill=BOTH, expand=True)

        self.mute = 0
        self.recording = 0

    def SetAudio(self, AudioComms):
        self.AudioComms = AudioComms

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
            self.recordButton.configure(relief='sunken')
            self.recording = 1
        elif self.recording == 1:
            self.AudioComms.start()
            self.recordButton.configure(relief='raised')
            self.recording = 0
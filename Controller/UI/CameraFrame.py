import cv2
import numpy as np
import imutils
from PIL import ImageTk, Image
from tkinter import *
from tkinter import Tk, LabelFrame, Label
from PIL import *


class CameraFrame(LabelFrame):
    def __init__(self, master, width, height, text, movementComms):
        super(CameraFrame, self).__init__(master, width = width, height = height, text = text)

        self._job1 = None
        self._job2 = None
        self.root = master
        self.movementComms = movementComms

        self.HorizontalSlider = Scale(self, from_=2500, to=500, orient =HORIZONTAL, command=self.updateHorizontal)
        self.VerticalSlider = Scale(self, from_=2500, to=500, command=self.updateVertical)
        self.CenterButton = Button(self, text="Center", command=self.center)
        
        self.HorizontalSlider.grid(row = 0, column = 1, sticky = NSEW)
        self.VerticalSlider.grid(row = 1, column = 0, sticky = NSEW)
        self.CenterButton.grid(row = 0, column = 0, sticky = NSEW, ipadx=2, ipady =2)

        self.HorizontalSlider.set(1500)
        self.VerticalSlider.set(1500)

        self.Video = Label(self, anchor ='nw',padx=0, pady=0)
        self.Video.grid(row=1, column=1, sticky='nsew',padx=5, pady=5)
        
        self.bind('<Configure>', self.resize)

        imgtk = ImageTk.PhotoImage(image= self.empty_image(480,640))
        self.Video.lmain = imgtk
        self.Video.configure(image=imgtk)
        self.LastImage = None
        
    def new_image(self, LastImage):
        if(self.LastImage is not None):
            self.LastImage = LastImage
        else:
            self.LastImage = LastImage
            self.video_stream()

    def video_stream(self, width = 480, height = 640):
        cv_image = cv2.cvtColor(self.LastImage, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(cv_image)

        imgtk = ImageTk.PhotoImage(image= pil_image)
        self.Video.lmain = imgtk
        self.Video.configure(image=imgtk)
        self.Video.after(10, self.video_stream)

    def resize(self, event):
        if(self.LastImage != None):
            self.video_stream(event.width, event.height)

    def empty_image(self, width, height):
        img_a = np.zeros([width,height,3],dtype=np.uint8)
        img_a.fill(55)
        img = Image.fromarray(img_a, 'RGB')
        return img

    def updateHorizontal(self, event):
        if self._job1:
            self.root.after_cancel(self._job1)

        self._job1 = self.root.after(500, self.sendUpdateHorizontalValue)

    def sendUpdateHorizontalValue(self):
        self.movementComms.CameraLeftRightSetValue(self.HorizontalSlider.get())

    def updateVertical(self, event):
        if self._job2:
            self.root.after_cancel(self._job2)

        self._job2 = self.root.after(500, self.sendUpdateVerticalValue)

    def sendUpdateVerticalValue(self):
        self.movementComms.CameraUpDownSetValue(self.VerticalSlider.get())

    def center(self):
        self.HorizontalSlider.set(1500)
        self.VerticalSlider.set(1500)
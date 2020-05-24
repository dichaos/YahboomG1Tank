import cv2
import numpy as np
import imutils
from PIL import ImageTk, Image
from tkinter import Tk, LabelFrame, Label
from UI.MovementFrame import MovementFrame
from PIL import *


class CameraFrame(LabelFrame):
    def __init__(self, master, width, height, text, movementComms):
        super(CameraFrame, self).__init__(master, width = width, height = height, text = text)

        self.CameraMovementPanel = MovementFrame(self, width=135, height=135, text="Movement",  movementComms=movementComms)
        self.CameraMovementPanel.grid(row=0, column=0,sticky='nw')
        #self.CameraMovementPanel.pack(side="left")

        self.CameraFrame = LabelFrame(self, width = 135, height = 145, text = "Video", padx=0, pady=0)
        #self.CameraFrame.pack(side="bottom", fill="both", expand = 1)
        self.CameraFrame.grid(row=0,column=1,sticky='nsew')
        
        self.Video = Label(self.CameraFrame, anchor ='nw',padx=0, pady=0)
        self.Video.grid(row=0, column=0, sticky='nsew',padx=5, pady=5)
        
        self.bind('<Configure>', self.resize)
        imgtk = ImageTk.PhotoImage(image= self.empty_image(200,200))
        self.Video.lmain = imgtk
        self.Video.configure(image=imgtk)
        self.LastImage = None
        
    def new_image(self, LastImage):
        if(self.LastImage is not None):
            self.LastImage = LastImage
        else:
            self.LastImage = LastImage
            self.video_stream()

    def video_stream(self, width = 200, height = 200):
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


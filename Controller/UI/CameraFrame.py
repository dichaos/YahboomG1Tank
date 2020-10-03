import cv2
import numpy as np
import imutils
from PIL import ImageTk, Image
from tkinter import *
from tkinter import Tk, LabelFrame, Label
from PIL import *
import FaceDetection.FaceDetection as FaceDetection
import traceback
from sys import platform


class CameraFrame(LabelFrame):
    def __init__(self, master):
        super(CameraFrame, self).__init__(master, width = 300, height = 140, text = "Camera", font=("Helvetica", 14))
        self.movementComms = None
        self._job1 = None
        self._job2 = None
        self.root = master

        self.HorizontalSlider = Scale(self, from_=180, to=0, width=35, orient =HORIZONTAL, command=self.updateHorizontal, showvalue='false')
        self.VerticalSlider = Scale(self, from_=180, to=0, width=35, command=self.updateVertical, showvalue='false')
        self.CenterButton = Button(self, text="Center", command=self.center,  font=("Helvetica", 14))
        
        self.HorizontalSlider.grid(row = 0, column = 1, sticky = EW+S)
        self.VerticalSlider.grid(row = 1, column = 0, sticky = NS+E)
        self.CenterButton.grid(row = 0, column = 0, sticky = NSEW, ipadx=2, ipady =2)

        self.HorizontalSlider.set(90)
        self.VerticalSlider.set(90)

        self.Video = Label(self, anchor ='nw',padx=0, pady=0)
        self.Video.grid(row=1, column=1, sticky='nsew',padx=5, pady=5)

        self.FaceRecognitionOpenCV = IntVar()
        self.OpenCVCheckBox = Checkbutton(self, text="OpenCV face detection", variable=self.FaceRecognitionOpenCV, font=("Helvetica", 14))
        self.OpenCVCheckBox.grid(row = 2, column=0, columnspan=2, sticky = NW)

        self.bind('<Configure>', self.resize)

        imgtk = ImageTk.PhotoImage(image= self.empty_image(480,640))
        self.Video.lmain = imgtk
        self.Video.configure(image=imgtk)
        self.LastImage = None

    def SetMovement(self, movementComms):
        self.movementComms = movementComms
        
    def new_image(self, LastImage):
        try:
            if(self.LastImage is not None):
                self.LastImage = LastImage
            else:
                self.LastImage = LastImage
                self.video_stream()
        except Exception as ex:
            traceback.print_exc()
            print(ex)

    def video_stream(self, width = 480, height = 640):
        cv_image = cv2.cvtColor(self.LastImage, cv2.COLOR_BGR2RGB)
        
        if self.FaceRecognitionOpenCV.get() == 1:
            cv_image = FaceDetection.detect(cv_image)

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
        if self.movementComms is not None:
            self.movementComms.CameraLeftRightSetValue(self.HorizontalSlider.get())

    def updateVertical(self, event):
        if self._job2:
            self.root.after_cancel(self._job2)

        self._job2 = self.root.after(500, self.sendUpdateVerticalValue)

    def sendUpdateVerticalValue(self):
        if self.movementComms is not None:
            self.movementComms.CameraUpDownSetValue(self.VerticalSlider.get())

    def center(self):
        self.HorizontalSlider.set(90)
        self.VerticalSlider.set(90)
        self.sendUpdateHorizontalValue()
        self.sendUpdateVerticalValue()


import cv2
import os
from sys import platform

def detect(image):
    path = os.getcwd()
    
    if platform == "win32":
        path = path + "\\FaceDetection\\"
    else:
        path = path +"/FaceDetection/"
        
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    haar_cascade_face = cv2.CascadeClassifier(path+"haarcascade_frontalface_default.xml")
    faces = haar_cascade_face.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)

    haar_cascade_profile = cv2.CascadeClassifier(path+"haarcascade_profileface.xml")

    profiles = haar_cascade_profile.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    for (x,y,w,h) in profiles:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return image

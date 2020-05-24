import socket
import zmq
import numpy as np
import cv2
from UI.MainWindow import *
import base64
import PIL.Image
import PIL.ImageTk
import traceback

class CameraStreamer:
    def __init__(self):
        self.context = zmq.Context()
        self.footage_socket = context.socket(zmq.PUB)
        self.footage_socket.connect('tcp://192.168.1.16:5555')

        self.camera = cv2.VideoCapture(0)  # init the camera
        
    def start(self):
        while True:
            try:
                frame = self.sock.recv_string()
                img = base64.b64decode(frame)
                npimg = np.fromstring(img, dtype=np.uint8)
                source = cv2.imdecode(npimg, 1)

                self.window.newImage(source)

            except Exception as e:
                traceback.print_exc()
                print(e)
                cv2.destroyAllWindows()
                break
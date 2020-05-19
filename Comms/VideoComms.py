import socket
import zmq
import numpy as np
import cv2
from UI.MainWindow import *
import base64
import PIL.Image
import PIL.ImageTk
import traceback

class VideoComms:
    def __init__(self, window):
        self.context = zmq.Context()
        self.sock = self.context.socket(zmq.SUB)
        self.sock.bind('tcp://*:5555')
        self.sock.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))
        
        self.window = window
        
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



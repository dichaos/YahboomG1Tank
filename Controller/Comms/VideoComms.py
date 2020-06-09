import socket
import zmq
import numpy as np
import cv2
from UI.MainWindow import *
import base64
import PIL.Image
import PIL.ImageTk
import traceback
import threading

class VideoComms:
    def __init__(self, url, window):
        self.window = window

        self.context = zmq.Context()
        self.sock = self.context.socket(zmq.SUB)
        self.sock.connect(url)
        self.sock.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))
        
        self.loop = 1
        
    def Loop(self):
        while self.loop == 1:
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

    def start(self):
        thread = threading.Thread(target=self.Loop)
        thread.daemon = True       
        thread.start()

    def stop(self):
        self.loop = 0



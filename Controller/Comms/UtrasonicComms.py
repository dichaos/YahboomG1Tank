import socket
import zmq
from UI.MainWindow import *
import base64
import traceback
import threading
import numpy as np

class UltrasonicComms:
    def __init__(self, url, window):
        self.window = window
        self.context = zmq.Context()
        self.sock = self.context.socket(zmq.SUB)
        self.sock.connect(url)
        self.sock.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))
        
    def Loop(self):
        while True:
            try:
                frame = self.sock.recv_string()
                self.window.ultraSonicValue(frame)

            except Exception as e:
                traceback.print_exc()
                print(e)
                break

    def start(self):
        thread = threading.Thread(target=self.Loop)
        thread.daemon = True       
        thread.start() 
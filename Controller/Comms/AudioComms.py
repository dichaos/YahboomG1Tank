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
import numpy as np
import pyaudio
import zmq

class AudioComms:
    def __init__(self, url):
        
        self.context = zmq.Context()
        self.sock = self.context.socket(zmq.SUB)
        self.sock.connect(url)
        self.sock.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))
        FS = 44100  # Hz
        self.pya = pyaudio.PyAudio()
        self.stream = self.pya.open(format=pyaudio.paInt16, channels=1, rate=FS, output=True)
        

        self.loop = 1
        
    def Loop(self):
        while self.loop == 1:
            try:
                frame = self.sock.recv_string()
                audio = base64.b64decode(frame)
                self.stream.write(audio)

            except Exception as e:
                traceback.print_exc()
                print(e)
                break

        self.stream.stop_stream()
        self.stream.close()
        self.pya.terminate()

    def start(self):
        self.loop = 1
        thread = threading.Thread(target=self.Loop)
        thread.daemon = True       
        thread.start()

    def stop(self):
        self.loop = 0
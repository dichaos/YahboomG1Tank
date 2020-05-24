import base64
import cv2
import zmq
import threading
import traceback

class VideoStreamer:
    def __init__(self, url):
        self.context = zmq.Context()
        self.footage_socket = self.context.socket(zmq.PUB)
        self.footage_socket.connect(url)

        self.camera = cv2.VideoCapture(0)  # init the camera
        self.loop = 0
    
    def Loop(self):
        while self.loop == 1:
            grabbed, frame = self.camera.read()  # grab the current frame
            encoded, buffer = cv2.imencode('.jpg', frame)
            jpg_as_text = base64.b64encode(buffer)
            self.footage_socket.send(jpg_as_text)
        
        self.camera.release()
        cv2.destroyAllWindows()
            
    def start(self):
        self.loop = 1
        self.thread = threading.Thread(target=self.Loop)
        self.thread.daemon = True       
        self.thread.start()

    def stop(self):
        self.loop = 0
        
import zmq
import threading
import base64
import cv2

class VideoRecorder():

    def __init__(self, sender, horizontalServo, verticalServo):
        self.sender = sender
        self.camera = cv2.VideoCapture(0)  # init the camera
        self.horizontalServo = horizontalServo
        self.verticalServo = verticalServo
        self.loop = 0

    def Loop(self):
        while self.loop == 1:
            grabbed, frame = self.camera.read()  # grab the current frame
            encoded, buffer = cv2.imencode('.jpg', frame)

            self.sender.base64Send(buffer)

        self.camera.release()
        cv2.destroyAllWindows()

    def start(self):
        self.loop = 1
        self.thread = threading.Thread(target=self.Loop)
        self.thread.daemon = True       
        self.thread.start()

    def stop(self):
        self.loop = 0
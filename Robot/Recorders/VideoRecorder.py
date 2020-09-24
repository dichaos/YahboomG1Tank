import base64
import cv2
import SensorReader

class VideoRecorder(SensorReader.SensorReader):

    def __init__(self, port):
        super(VideoRecorder, self).__init__()
        self.camera = cv2.VideoCapture(0)  # init the camera
        self.port = port

    def ReadValue(self):
        grabbed, frame = self.camera.read()  # grab the current frame
        encoded, buffer = cv2.imencode('.jpg', frame)

        return base64.b64encode(buffer)
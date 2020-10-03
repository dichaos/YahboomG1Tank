import base64
import cv2
import SensorReader

class VideoRecorder(SensorReader.SensorReader):

    def __init__(self, port):
        super(VideoRecorder, self).__init__()
        self.camera = cv2.VideoCapture(0)
        self.port = port

    def ReadValue(self):
        grabbed, frame = self.camera.read()

        if(grabbed == True):
            ncode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            encoded, buffer = cv2.imencode('.jpg', frame, ncode_param)
            return base64.b64encode(buffer)
        else:
            print("failed to grab frame")

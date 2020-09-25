import numpy as np
import cv2
import base64
import Comms.Sockets.UDPReader as UDPReader

class VideoComms(UDPReader.UDPReader):
    def __init__(self, port, window):
        super(VideoComms, self).__init__(port)
        self.window = window

    def Process(self, value):
        img = base64.b64decode(value)
        npimg = np.fromstring(img, dtype=np.uint8)
        source = cv2.imdecode(npimg, 1)
        self.window.newImage(source)
    
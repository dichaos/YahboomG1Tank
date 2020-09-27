import numpy as np
import cv2
import base64
import Comms.Sockets.UDPReader as UDPReader
import Comms.Recorder.Recorder as Recorder

class VideoComms(UDPReader.UDPReader, Recorder.Recorder):
    def __init__(self, port, window):
        super().__init__(port)
        super(UDPReader.UDPReader, self).__init__()
        self.window = window
        self.record = 0
        
    def Process(self, value):
        img = base64.b64decode(value)
        npimg = np.fromstring(img, dtype=np.uint8)
        source = cv2.imdecode(npimg, 1)
        self.window.newImage(source)

        if self.record == 1 and hasattr(self, 'out') and self.out is not None:
            self.out.write(source)

    def Record(self):
        super().Record()
        fourcc = cv2.VideoWriter_fourcc(*'MPEG')
        self.out = cv2.VideoWriter('video.mpeg', fourcc, 20, (640,480))
        print(self.out)
            
    def RecordStop(self):
        super().RecordStop()
        self.out.release()

    def stop(self):
        super().stop()
        cv2.destroyAllWindows()
    
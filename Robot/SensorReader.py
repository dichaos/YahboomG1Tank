import abc
import Comms.UDPSender as UDPSender
import threading
import time

class SensorReader(UDPSender.UDPSender):
    
    def _init_(self):
        super(SensorReader, self).__init__()

    @abc.abstractmethod
    def ReadValue(self):
        pass

    def Loop(self):
        while self.loop == 1:
            track = self.ReadValue()
            self.Send(track)
        
    def start(self):
        self.loop = 1
        thread = threading.Thread(target=self.Loop)
        thread.daemon = True       
        thread.start()

    def stop(self):
        self.loop = 0

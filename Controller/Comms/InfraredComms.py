import Comms.Sockets.UDPReader as UDPReader

class InfraredComms(UDPReader.UDPReader):
    def __init__(self, port, window):
        super(InfraredComms, self).__init__(port)
        self.window = window
        
    def Process(self, value):
        self.window.TrackValue(value)
    
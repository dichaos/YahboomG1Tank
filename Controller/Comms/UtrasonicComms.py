import Comms.Sockets.UDPReader as UDPReader

class UltrasonicComms(UDPReader.UDPReader):
    def __init__(self, port, window):
        super(UltrasonicComms, self).__init__(port)
        self.window = window

    def Process(self, value):
        self.window.ultraSonicValue(value)

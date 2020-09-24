import base64
import socket
import math
import struct

class Streamer:

    def __init__(self, port):
        self.port = port
        self.MAX_DGRAM = 2**16
        self.MAX_IMAGE_DGRAM = self.MAX_DGRAM - 64 
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(("127.0.0.1", self.port))

    def Send(self, value):
        size = len(value)
        count = math.ceil(size/(self.MAX_IMAGE_DGRAM))
        array_pos_start = 0

        while count:
            array_pos_end = min(size, array_pos_start + self.MAX_IMAGE_DGRAM)
            self.s.sendto(struct.pack("B", count)+value[array_pos_start:array_pos_end], ("127.0.0.1", self.port))
            array_pos_start = array_pos_end
            count -= 1

        self.s.send_string(value)

    def base64Send(self, value):
        as_text = base64.b64encode(value.read())
        self.Send(as_text)


    def close(self):
        s.close()
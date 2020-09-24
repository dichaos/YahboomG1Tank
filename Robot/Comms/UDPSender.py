import base64
import socket
import math
import struct

class UDPSender:
    
    def __init__(self):
        self.MAX_DGRAM = 2**16
        self.MAX_IMAGE_DGRAM = self.MAX_DGRAM - 64 
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.ip = ""
        self.port = 0

    def SetIp(self, ip):
        self.ip = ip

    def Send(self, value):

        if self.ip == "":
            return

        size = len(value)
        count = math.ceil(size/(self.MAX_IMAGE_DGRAM))
        array_pos_start = 0

        while count:
            array_pos_end = min(size, array_pos_start + self.MAX_IMAGE_DGRAM)

            self.s.sendto(struct.pack("B", count)+value[array_pos_start:array_pos_end], (ip, port))
            array_pos_start = array_pos_end
            count -= 1

    def base64Send(self, value):
        as_text = base64.b64encode(value)
        self.Send(as_text)

    def Stop(self):
        self.s.close()
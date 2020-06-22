import zmq
import base64

class Streamer:
    def __init__(self, url):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind(url)

    def Send(self, value):
        self.socket.send_string(value)

    def base64Send(self, value):
        as_text = base64.b64encode(value)
        self.socket.send(as_text)


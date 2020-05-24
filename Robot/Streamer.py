import zmq

class Streamer:
    def __init__(self, url):
        self.context = zmq.Context()
        self.footage_socket = self.context.socket(zmq.PUB)
        self.footage_socket.connect(url)

    def Send(self, value):
        self.footage_socket.send_string(value)

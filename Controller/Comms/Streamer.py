import zmq

class Streamer:
    def __init__(self, url):
        self.context = zmq.Context()
        self.footage_socket = self.context.socket(zmq.PAIR)
        self.footage_socket.bind(url)

    def Send(self, value):
        self.footage_socket.send_string(value)
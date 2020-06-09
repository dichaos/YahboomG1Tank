import zmq

class Streamer:
    def __init__(self, url):
        self.url = url

    def start(self):
        self.context = zmq.Context()
        self.footage_socket = self.context.socket(zmq.PAIR)
        self.footage_socket.connect(self.url)

    def startUrl(self, url):
        self.url = url 
        self.start()
        

    def Send(self, value):
        self.footage_socket.send_string(value)
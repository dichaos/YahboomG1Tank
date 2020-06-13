import zmq
import base64

class AudioStreamer():
    def __init__(self, url):
        self.context = zmq.Context()

        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind(url)

    def send(self, buf):
        audio_as_text = base64.b64encode(buf)
        self.socket.send(audio_as_text)

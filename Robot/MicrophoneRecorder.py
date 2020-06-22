import numpy as np
import pyaudio
import zmq
import threading

#FS = 44100  # Hz
#CHUNKSZ = 4096  # samples

class MicrophoneRecorder():

    def __init__(self, sender):
        self.sender = sender
        self.p = pyaudio.PyAudio()

        form_1 = pyaudio.paInt16 # 16-bit resolution
        chans = 1 # 1 channel
        samp_rate = 44100 # 44.1kHz sampling rate
        self.chunk = 8192 # 2^12 samples for buffer
        record_secs = 3 # seconds to record
        dev_index = 0 # device index found by p.get_device_info_by_index(ii)

        devinfo = self.p.get_device_info_by_index(0)
        print(devinfo)

        self.stream = self.p.open(format = form_1,rate = samp_rate,channels = chans, \
                    input_device_index = dev_index,input = True, \
                    frames_per_buffer=self.chunk)



        self.loop = 0

    def read(self):
        data = self.stream.read(self.chunk, exception_on_overflow = False)
        self.sender.base64Send(data)

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def Loop(self):
        while self.loop == 1:
            self.read()

    def start(self):
        self.loop = 1
        self.thread = threading.Thread(target=self.Loop)
        self.thread.daemon = True       
        self.thread.start()

    def stop(self):
        self.loop = 0
        
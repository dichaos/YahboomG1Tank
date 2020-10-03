import numpy as np
from ctypes import *
import os
import pyaudio
import SensorReader
import base64

def py_error_handler(filename, line, function, err, fmt):
    return

def suppressPyAudioErrors():
    ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
    c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
    asound = cdll.LoadLibrary('libasound.so')
    # Set error handler
    asound.snd_lib_error_set_handler(c_error_handler)

class MicrophoneRecorder(SensorReader.SensorReader):

    def __init__(self, port):
        super(MicrophoneRecorder, self).__init__()
        suppressPyAudioErrors()
        self.p = pyaudio.PyAudio()

        form_1 = pyaudio.paInt16 # 16-bit resolution
        chans = 1 # 1 channel
        samp_rate = 48000 # 44.1kHz sampling rate
        self.chunk = 8192 # 2^12 samples for buffer
        record_secs = 1 # seconds to record
        dev_index = 0 # device index found by p.get_device_info_by_index(ii)

        #print("===============Audio device====================")
        #print(self.p.get_device_info_by_index(1))
        #print("-----------------------------------------------")
        #self.getaudiodevices()

        self.stream = self.p.open(format = form_1,
                                    rate = samp_rate, 
                                    channels = chans, 
                                    input_device_index = dev_index, 
                                    input = True, 
                                    frames_per_buffer=self.chunk)

        self.port = port

    def getaudiodevices(self):
        devices = os.popen("arecord -l")
        device_string = devices.read()
        device_string = device_string.split("\n")
        for line in device_string:
            if(line.find("card") != -1):
                print(line + ",\n")

    def ReadValue(self):
        data = self.stream.read(self.chunk, exception_on_overflow = False)
        return base64.b64encode(data)

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

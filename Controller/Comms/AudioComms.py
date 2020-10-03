import base64
import traceback
import pyaudio
import wave
import Comms.Sockets.UDPReader as UDPReader
import Comms.Recorder.Recorder as Recorder
import traceback

class AudioComms(UDPReader.UDPReader, Recorder.Recorder):
    def __init__(self, port):
        super().__init__(port)
        super(UDPReader.UDPReader, self).__init__()
        
        self.resolution = pyaudio.paInt16 # 16-bit resolution
        self.channels = 1 # 1 channel
        self.rate = 48000 # 44.1kHz sampling rate
        self.chunk = 8192 # 2^12 samples for buffer
        
        self.frames = []
        
    def Process(self, value):
        try:
            audio = base64.b64decode(value)

            if self.record == 1:
                self.frames.append(audio)

            self.stream.write(audio, self.chunk)

        except Exception as e:
            traceback.print_exc()
            print(e)
            self.stop()

    def start(self):
        try:
            self.pya = pyaudio.PyAudio()

            print("===============Audio device====================")
            for ii in range(self.pya.get_device_count()):
                print(self.pya.get_device_info_by_index(ii).get('name'))
            print("-----------------------------------------------")

            self.stream = self.pya.open(format=self.resolution,
                                        rate=self.rate,  
                                        channels=self.channels, 
                                        output=True)

            super(AudioComms, self).start()
        except Exception as e:
            traceback.print_exc()
            print(e)
               
    def stop(self):
        try:
            super(AudioComms, self).stop()
            self.pya.terminate()
        except Exception as e:
            traceback.print_exc()
            print(e)

    def Record(self):
        super().Record()
        
        if self.record == 0:
            self.frames = []
            
    def RecordStop(self):
        super().RecordStop()
        
        wf = wave.open("audio.wav", 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.pya.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(self.frames))
        wf.close()

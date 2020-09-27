import base64
import traceback
import pyaudio
import wave
import Comms.Sockets.UDPReader as UDPReader
import Comms.Recorder.Recorder as Recorder

class AudioComms(UDPReader.UDPReader, Recorder.Recorder):
    def __init__(self, port):
        super().__init__(port)
        super(UDPReader.UDPReader, self).__init__()
        self.FS = 44100  # Hz
        self.frames = []
        
    def Process(self, value):
        try:
            audio = base64.b64decode(value)

            if self.record == 1:
                self.frames.append(audio)

            self.stream.write(audio)
        except Exception as e:
            traceback.print_exc()
            print(e)
            self.stop()

    def start(self):
        self.pya = pyaudio.PyAudio()
        self.stream = self.pya.open(format=pyaudio.paInt16, channels=1, rate=self.FS, output=True)
        super(AudioComms, self).start()
        
    def stop(self):
        super(AudioComms, self).stop()
        self.pya.terminate()

    def Record(self):
        super().Record()
        
        if self.record == 0:
            self.frames = []
            
    def RecordStop(self):
        super().RecordStop()
        
        wf = wave.open("Audio.wav", 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.pya.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(self.frames))
        wf.close()

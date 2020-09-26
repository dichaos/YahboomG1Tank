import base64
import traceback
import pyaudio
import wave
import Comms.Sockets.UDPReader as UDPReader

class AudioComms(UDPReader.UDPReader):
    def __init__(self, port):
        super(AudioComms, self).__init__(port)
        self.FS = 44100  # Hz
        self.record = 0
        self.frames = []
        
    def Process(self, value):
        try:
            audio = base64.b64decode(value)

            if self.record == 1:
                print("recoded audio")
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
        if self.record == 0:
            self.frames = []
            self.record = 1

    def RecordStop(self, filename):
        if self.record == 1:
            self.record = 0
            wf = wave.open(filename, 'wb')
            wf.setnchannels(1)
            wf.setsampwidth(self.pya.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b''.join(self.frames))
            wf.close()

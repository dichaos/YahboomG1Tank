import abc

class Recorder:
    def __init__(self):
        self.record = 0

    def Record(self):
        if self.record == 0:
            self.record = 1

    def RecordStop(self):
        if self.record == 1:
            self.record = 0

    @abc.abstractmethod
    def ProcessRecord(self, value):
        pass
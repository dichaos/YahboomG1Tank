class DesktoEvents():

    def __init__(self, comms):
        self.socket = comms

    def MoveForward(self, event):
        print("Single Click, Move Forward")
        self.socket.Send("Forward")

    def MoveBackwards(self, event):
        print("Single Click, Move Back")
        self.socket.Send("Back")

    def MoveLeft(self, event):
        print("Single Click, Move Left")
        self.socket.Send("Left")

    def MoveRight(self, event):
        print("Single Click, Move Right")
        self.socket.Send("Right")

    def MoveStop(self, event):
        print("Single Click, Move Stopped")
        self.socket.Send("Stop")
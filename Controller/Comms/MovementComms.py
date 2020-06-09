class MovementComms():

    def __init__(self, comms):
        self.socket = comms

    def MoveStop(self):
        self.socket.Send("Move Stopped")

    def MoveForward(self):
        self.socket.Send("Move Forward")

    def MoveBackwards(self):
        self.socket.Send("Move Backwards")

    def MoveLeft(self):
        self.socket.Send("Turn Left")

    def MoveRight(self):
        self.socket.Send("Turn Right")

    def LeftMotorForward(self):
        self.socket.Send("LeftMotor Forward")
    
    def LeftMotorBackwards(self):
        self.socket.Send("LeftMotor Backwards")

    def RightMotorForward(self):
        self.socket.Send("RightMotor Forward")
    
    def RightMotorBackwards(self):
        self.socket.Send("RightMotor Backwards")

    def SetSpeed(self, speed):
        self.socket.Send("Speed:"+str(speed))

    def CameraUpDownSetValue(self, value):
        self.socket.Send("CameraUpDown:"+str(value))

    def CameraLeftRightSetValue(self, value):
        self.socket.Send("CameraLeftRight:"+str(value))

    def UltrsonicSetValue(self, value):
        self.socket.Send("Ultra:"+str(value))
    
    def SendColor(self, red, green, blue):
        self.socket.Send("Color:"+str(red)+","+str(green)+","+str(blue))

    def BuzzOn(self):
        self.socket.Send("BuzzOn")
    
    def BuzzOff(self):
        self.socket.Send("BuzzOff")

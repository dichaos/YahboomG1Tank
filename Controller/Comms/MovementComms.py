import Comms.Sockets.SocketClient as SocketClient

class MovementComms(SocketClient.SocketClient):

    def __init__(self, ip, port):
        super(MovementComms, self).__init__(ip, port)

    def MoveStop(self):
        self.send("Move Stopped")

    def MoveForward(self):
        self.send("Move Forward")

    def MoveBackwards(self):
        self.send("Move Backwards")

    def MoveLeft(self):
        self.send("Turn Left")

    def MoveRight(self):
        self.send("Turn Right")

    def LeftMotorForward(self):
        self.send("LeftMotor Forward")
    
    def LeftMotorBackwards(self):
        self.send("LeftMotor Backwards")

    def RightMotorForward(self):
        self.send("RightMotor Forward")
    
    def RightMotorBackwards(self):
        self.send("RightMotor Backwards")

    def SetSpeed(self, speed):
        self.send("Speed:"+str(speed))

    def CameraUpDownSetValue(self, value):
        self.send("CameraUpDown:"+str(value))

    def CameraLeftRightSetValue(self, value):
        self.send("CameraLeftRight:"+str(value))

    def UltrsonicSetValue(self, value):
        self.send("Ultra:"+str(value))
    
    def SendColor(self, red, green, blue):
        self.send("Color:"+str(red)+","+str(green)+","+str(blue))

    def BuzzOn(self):
        self.send("BuzzOn")
    
    def BuzzOff(self):
        self.send("BuzzOff")

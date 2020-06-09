class MovementComms():

    def __init__(self, comms):
        self.socket = comms

    def MoveStop(self):
        print("Move Stopped")
        self.socket.Send("Move Stopped")

    def MoveForward(self):
        print("Move Forward")
        self.socket.Send("Move Forward")

    def MoveBackwards(self):
        print("Move Backwards")
        self.socket.Send("Move Backwards")

    def MoveLeft(self):
        print("Turn Left")
        self.socket.Send("Turn Left")

    def MoveRight(self):
        print("Turn Right")
        self.socket.Send("Turn Right")

    def LeftMotorForward(self):
        print("LeftMotor Forward")
        self.socket.Send("LeftMotor Forward")
    
    def LeftMotorBackwards(self):
        print("LeftMotor Backwards")
        self.socket.Send("LeftMotor Backwards")

    def RightMotorForward(self):
        print("RightMotor Forward")
        self.socket.Send("RightMotor Forward")
    
    def RightMotorBackwards(self):
        print("RightMotor Backwards")
        self.socket.Send("RightMotor Backwards")

    def SetSpeed(self, speed):
        print("SetSpeed = ", speed)
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

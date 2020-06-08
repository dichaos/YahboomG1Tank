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
        self.socket.Send("Speed=" + str(speed))

    def CameraUp(self):
        print("CameraUp")
        self.socket.Send("CameraUp")

    def CameraDown(self):
        print("CameraDown")
        self.socket.Send("CameraDown")

    def CameraLeft(self):
        print("CameraLeft")
        self.socket.Send("CameraLeft")
    
    def CameraRight(self):
        print("CameraRight")
        self.socket.Send("CameraRight")

    def CameraReset(self):
        print("CameraReset")
        self.socket.Send("CameraReset")

    def CameraUpDownStop(self):
        print("Camera Up Down stop")
        self.socket.Send("CameraUpDownStop")

    def CameraLeftRightStop(self):
        print("Camera Left Right stop")
        self.socket.Send("CameraLeftRightStop")

    def UltrsonicSetValue(self, value):
        strValue = "Ultra:"+str(value)
        print('before sent')
        self.socket.Send(strValue)
        print('sent')


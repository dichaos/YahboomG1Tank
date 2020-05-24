class MovementComms():

    def __init__(self, comms):
        self.socket = comms

    def MoveStop(self):
        print("Move Stopped")
        self.socket.Send("Motor=0")

    def MoveForward(self):
        print("Move Forward")
        self.socket.Send("Motor=1")

    def MoveBackwards(self):
        print("Move Backwards")
        self.socket.Send("Motor=2")

    def MoveLeft(self):
        print("Turn Left")
        self.socket.Send("Motor=3")

    def MoveRight(self):
        print("Turn Right")
        self.socket.Send("Motor=4")

    def LeftMotorForward(self):
        print("LeftMotor Forward")
        self.socket.Send("Motor=4")
    
    def LeftMotorBackwards(self):
        print("LeftMotor Backwards")
        self.socket.Send("Motor=5")

    def RightMotorForward(self):
        print("LeftMotor Forward")
        self.socket.Send("Motor=6")
    
    def RightMotorBackwards(self):
        print("LeftMotor Backwards")
        self.socket.Send("Motor=7")

    def SetSpeed(self, speed):
        print("SetSpeed = ", speed)
        self.socket.Send("Speed=" + str(speed))


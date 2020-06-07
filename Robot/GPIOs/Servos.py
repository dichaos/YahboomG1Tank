import pigpio
import time
import threading

class Servo:
    def __init__(self, servoPin):
        self.servoPin = servoPin
        self.pig = pigpio.pi()
        self.pig.set_mode(servoPin, pigpio.OUTPUT)

    def rotate(self, angle):
        if angle > 2500:
            angle = 2500
        if angle < 500:
            angle = 0

        self.pig.set_servo_pulsewidth(self.servoPin, angle)
        time.sleep(1)

    def stop(self):
        self.pig.set_servo_pulsewidth(self.servoPin, 0)
        self.pig.stop()
        
class UltrasonicServo(Servo):
    def __init__(self):
        super().__init__(23)
        self.Forward()

    def Forward(self):
        self.rotate(1500)

class CameraHorizontalServo(Servo):
    def __init__(self):
        super().__init__(11)
        self.Forward()
        self.Current = 1500
        self.MoveUpDown = 1
        self.Direction = 'Stop'

        thread = threading.Thread(target=self.MoveLeftRightLoop)
        thread.daemon = True       
        thread.start() 

    def Forward(self):
        self.rotate(1500)

    def MoveLeftRightLoop(self):
        while self.MoveUpDown == 1:
            if self.Direction == 'left':
                self.Current = self.Current + 25
            elif self.Direction == 'right': 
                self.Current = self.Current - 25

            self.rotate(self.Current)
            time.sleep(0.1)

    def Stop(self):
        self.Direction = 'Stop'

    def StartMoveLeft(self):
        self.Direction ='left'

    def StartMoveRight(self):
        self.Direction ='right'

class CameraVerticalServo(Servo):
    def __init__(self):
        super().__init__(9)
        self.Forward()
        self.Current = 1500
        self.MoveUpDown = 1
        self.Direction = 'Stop'

        thread = threading.Thread(target=self.MoveUpDownLoop)
        thread.daemon = True       
        thread.start() 
    
    def Forward(self):
        self.rotate(1500)

    def MoveUpDownLoop(self):
        while self.MoveUpDown == 1:
            if self.Direction == 'up':
                self.Current = self.Current + 25
            elif self.Direction == 'down': 
                self.Current = self.Current - 25

            self.rotate(self.Current)
            time.sleep(0.1)

    def Stop(self):
        self.Direction = 'Stop'

    def StartMoveUp(self):
        self.Direction ='up'

    def StartMoveDown(self):
        self.Direction ='down'
         


        



    
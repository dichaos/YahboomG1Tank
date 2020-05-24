import pigpio
import time

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
        self.rotate(2000)

class CameraHorizontalServo(Servo):
    def __init__(self):
        super().__init__(11)
        self.Forward()

    def Forward(self):
        self.rotate(2000)

class CameraVerticalServo(Servo):
    def __init__(self):
        super().__init__(9)
        self.Forward()

    def Forward(self):
        self.rotate(1700)



    
import pigpio
import time
import threading

class Servo:
    pulse_value = 0

    def __init__(self, servoPin):
        self.servoPin = servoPin
        self.pig = pigpio.pi()
        self.pig.set_mode(servoPin, pigpio.OUTPUT)

    def rotate(self, angle):
        if angle > 2500:
            angle = 2500
        if angle < 500:
            angle = 0

        self.pulse_value = angle

        self.pig.set_servo_pulsewidth(self.servoPin, angle)
        time.sleep(1)

    def stop(self):
        self.pig.set_servo_pulsewidth(self.servoPin, 0)
        self.pig.stop()

    def ConvertRadsInPulseWidth(self, angle):
        everyRadianInPulseWidth = 439.267642
        rounded = "{:.10f}".format(float(angle))
        pulseWithFromRadians = (everyRadianInPulseWidth * float(rounded))

        moveFromCentre= 1435 + pulseWithFromRadians
        return moveFromCentre

    def ConvertPulseWidthInRads(self, angle):
        everyRadianInPulseWidth = 439.267642
        return angle/everyRadianInPulseWidth
        
class UltrasonicServo(Servo):
    def __init__(self):
        super().__init__(23)
        self.Forward()

    def Forward(self):
        self.rotate(1500)

    def Set(self, value):
        self.rotate(value)
    
class CameraHorizontalServo(Servo):
    def __init__(self):
        super().__init__(11)
        self.Forward()
        
    def Forward(self):
        self.rotate(1500)

    def Set(self, value):
        self.value = value
        self.rotate(value)

class CameraVerticalServo(Servo):
    def __init__(self):
        super().__init__(9)
        self.Forward()

    def Forward(self):
        self.rotate(1500)

    def Set(self, value):
        self.value = value
        self.rotate(value)
    
import pigpio
import time
import threading

class Servo:
    def __init__(self, servoPin):
        self.servoPin = servoPin
        self.pig = pigpio.pi()
        self.pig.set_mode(servoPin, pigpio.OUTPUT)

    def rotate(self, angle):
        self.angle_value = angle
        pulse = self.ConvertRadsInPulseWidth(angle)
        self.setPulse(pulse)

    def setPulse(self, pulse):
        if pulse > 2500:
            pulse = 2500
        if pulse < 500:
            pulse = 0

        self.pulse_value = pulse
        self.pig.set_servo_pulsewidth(self.servoPin, pulse)
        time.sleep(1)

    def stop(self):
        self.pig.set_servo_pulsewidth(self.servoPin, 0)
        self.pig.stop()

    def ConvertRadsInPulseWidth(self, angle):
        return ((2000*angle)/180) + 500

    def ConvertPulseWidthInRads(self, pulse):
        return (180*(pulse-500))/2000

class UltrasonicServo(Servo):
    def __init__(self):
        super().__init__(9)
        self.Forward()

    def Forward(self):
        self.rotate(90)

    def Set(self, value):
        self.rotate(value)
    
class CameraHorizontalServo(Servo):
    def __init__(self):
        super().__init__(11)
        self.Forward()
        
    def Forward(self):
        self.rotate(90)

    def Set(self, value):
        self.value = value
        self.rotate(value)

class CameraVerticalServo(Servo):
    def __init__(self):
        super().__init__(23)
        self.Forward()

    def Forward(self):
        self.rotate(90)

    def Set(self, value):
        self.value = value
        self.rotate(value)
    
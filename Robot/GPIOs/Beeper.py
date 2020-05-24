import RPi.GPIO as GPIO

class Beeper:
    def __init__(self):
        self.Beeper = 8
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Beeper,GPIO.OUT)
        GPIO.output(self.Beeper, GPIO.HIGH)
        self.onoff = 0

    def Beep(self):
        self.onoff = 1
        GPIO.output(self.Beeper,GPIO.LOW)

    def stop(self):
        if self.onoff == 1:
            print("Stopping beeper")
            GPIO.output(self.Beeper, GPIO.HIGH)
            GPIO.cleanup()
        
        
import RPi.GPIO as GPIO
import time
import threading
import traceback
import SensorReader

class Ultrasonic(SensorReader.SensorReader):
    def __init__(self, port):
        super(Ultrasonic, self).__init__()
        self.EchoPin = 0
        self.TrigPin = 1

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.EchoPin,GPIO.IN)
        GPIO.setup(self.TrigPin,GPIO.OUT)

        self.port = port


    def ReadValue(self):
        time.sleep(1)
        # set Trigger to HIGH
        GPIO.output(self.TrigPin, True)
    
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.TrigPin, False)
    
        StartTime = time.time()
        StopTime = time.time()
    
        # save StartTime
        while GPIO.input(self.EchoPin) == 0:
            StartTime = time.time()
    
        # save time of arrival
        while GPIO.input(self.EchoPin) == 1:
            StopTime = time.time()
    
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
    
        toReturn = str(round(distance,2)).encode()
        return toReturn


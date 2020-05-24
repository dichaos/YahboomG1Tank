import RPi.GPIO as GPIO
import time
import threading
import traceback

class Ultrasonic:
    def __init__(self, streamer = None):
        self.EchoPin = 0
        self.TrigPin = 1
        self.streamer = streamer
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.EchoPin,GPIO.IN)
        GPIO.setup(self.TrigPin,GPIO.OUT)
        self.loop = 0

    def distance(self):
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
    
        return distance
    
    def Loop(self):
        while self.loop == 1:
            dist = self.distance()
            
            if self.streamer is not None:
                self.streamer.Send(str(dist))

            print ("Distance = %.1f cm" % dist)
            time.sleep(1)
        
        GPIO.cleanup()

    def start(self):
        self.loop = 1
        thread = threading.Thread(target=self.Loop)
        thread.daemon = True       
        thread.start()

    def stop(self):
        self.loop = 0
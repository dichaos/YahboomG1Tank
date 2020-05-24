import RPi.GPIO as GPIO
import threading
import time

class TrackSensor:
    def __init__(self, streamer = None):
        self.streamer = streamer
        self.TrackSensorLeftPin1  =  3   #The first tracking infrared sensor pin on the left is connected to  BCM port 3 of Raspberry pi
        self.TrackSensorLeftPin2  =  5   #The second tracking infrared sensor pin on the left is connected to  BCM port 5 of Raspberry pi
        self.TrackSensorRightPin1 =  4   #The first tracking infrared sensor pin on the right is connected to  BCM port 4 of Raspberry pi
        self.TrackSensorRightPin2 =  18   #The second tracking infrared sensor pin on the right is connected to  BCM port 18 of Raspberry pi

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.TrackSensorLeftPin1,GPIO.IN)
        GPIO.setup(self.TrackSensorLeftPin2,GPIO.IN)
        GPIO.setup(self.TrackSensorRightPin1,GPIO.IN)
        GPIO.setup(self.TrackSensorRightPin2,GPIO.IN)
        self.loop = 0

    def tracking_test(self):
        #When the black line is detected, the corresponding indicator of the tracking module is on, and the port level is LOW.
        #When the black line is not detected, the corresponding indicator of the tracking module is off, and the port level is HIGH.
        TrackSensorLeftValue1  = GPIO.input(self.TrackSensorLeftPin1)
        TrackSensorLeftValue2  = GPIO.input(self.TrackSensorLeftPin2)
        TrackSensorRightValue1 = GPIO.input(self.TrackSensorRightPin1)
        TrackSensorRightValue2 = GPIO.input(self.TrackSensorRightPin2)
        infrared_track_value_list = ['0','0','0','0']
        infrared_track_value_list[0] = str(1^ TrackSensorLeftValue1)
        infrared_track_value_list[1] =str(1^ TrackSensorLeftValue2)
        infrared_track_value_list[2] = str(1^ TrackSensorRightValue1)
        infrared_track_value_list[3] = str(1^ TrackSensorRightValue2)
        return ''.join(infrared_track_value_list)
    
    def Loop(self):
        while self.loop == 1:
            track = self.tracking_test()
            
            if self.streamer is not None:
                self.streamer.Send(track)

            print ("Tracking = " , track)
            time.sleep(1)
        
        GPIO.cleanup()

    def start(self):
        self.loop = 1
        thread = threading.Thread(target=self.Loop)
        thread.daemon = True       
        thread.start()

    def stop(self):
        self.loop = 0
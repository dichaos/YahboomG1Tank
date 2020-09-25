import time
import atexit
import RPi.GPIO as GPIO
import Comms.CommsManager as CommsManager
import Comms.RobotSocketServer as RobotSocketServer

def cleanup(robotSocketServer):
    CommsManager.Cleanup()
    robotSocketServer.stop()
    GPIO.cleanup()
    print("cleaned up")
                                        
robotSocketServer = RobotSocketServer.RobotSocketServer()
robotSocketServer.start(9999)

CommsManager.buzzer.Buzz()
time.sleep(0.5)
CommsManager.buzzer.stop()
print("All started")

atexit.register(cleanup, robotSocketServer)
k=input("press close to exit") 


 
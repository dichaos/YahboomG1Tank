import time
import atexit
import RPi.GPIO as GPIO
import Comms.CommsManager as CommsManager
import Comms.RobotSocketServer as RobotSocketServer
import Comms.UDPSender as UDPServer
import GPIOs.Buzzer as Buzzer
import GPIOs.LEDs as LEDs
import GPIOs.Servos as Servos
import GPIOs.TankMovement as TankMovement
import GPIOs.TrackSensor as TrackSensor
import GPIOs.Ultrasonic as Ultrasonic
import Recorders.MicrophoneRecorder as MicrophoneRecorder
import Recorders.VideoRecorder as VideoRecorder


buzzer = Buzzer.Buzzer()
led = LEDs.LEDs()

movement = TankMovement.TankMovement()
ultraSonicMover = Servos.UltrasonicServo()
cameraHorizontal = Servos.CameraHorizontalServo()
cameraVertical = Servos.CameraVerticalServo()
ultrasonicSensor = Ultrasonic.Ultrasonic(1000)
trackSensor = TrackSensor.TrackSensor(1001)
videoRecorder = VideoRecorder.VideoRecorder(1002)
microphoneRecorder = MicrophoneRecorder.MicrophoneRecorder(1003)

commsManager = CommsManager.CommsManager(movement, 
                                        cameraVertical, 
                                        cameraHorizontal, 
                                        ultraSonicMover, 
                                        led, 
                                        buzzer, 
                                        trackSensor, 
                                        ultrasonicSensor, 
                                        videoRecorder, 
                                        microphoneRecorder)
                                        
robotSocketServer = RobotSocketServer.RobotSocketServer()

robotSocketServer.start(9999, commsManager)

trackSensor.start()
ultrasonicSensor.start()
videoRecorder.start()
microphoneRecorder.start()

buzzer.Buzz()
time.sleep(0.5)
buzzer.stop()
print("All started")

def cleanup(buzzer,
            led,
            movement,
            ultraSonicMover,
            cameraHorizontal,
            cameraVertical,
            ultrasonicSensor,
            trackSensor,
            videoRecorder,
            microphoneRecorder,
            robotSocketServer):
    GPIO.cleanup()
    buzzer.stop()
    led.TurnOff()
    ultraSonicMover.stop()
    cameraHorizontal.stop()
    cameraVertical.stop()
    ultrasonicSensor.stop()
    trackSensor.stop()
    videoRecorder.stop()
    microphoneRecorder.stop()
    robotSocketServer.stop()
    microphoneRecorder.close()
    print("cleaned up")


atexit.register(cleanup, 
                buzzer,
                led,
                movement,
                ultraSonicMover,
                cameraHorizontal,
                cameraVertical,
                ultrasonicSensor,
                trackSensor,
                videoRecorder,
                microphoneRecorder,
                robotSocketServer
                )

k=input("press close to exit") 


 
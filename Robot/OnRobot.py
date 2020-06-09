import GPIOs.TankMovement as TankMovement
import GPIOs.Servos as Servos
import GPIOs.LEDs as LED
import GPIOs.Buzzer as Buzzer
import GPIOs.Ultrasonic as Ultrasonic
import GPIOs.TrackSensor as TrackSensor
import VideoStreamer
import Streamer
import time
import atexit
import RPi.GPIO as GPIO
import Comms.MovementComms as movementComms


def cleanup(servo1, servo2, servo3, led, beeper, video, track, movement, ultrasonicreader):
    movement.stop()
    servo1.stop()
    servo2.stop()
    servo3.stop()
    led.TurnOff()
    beeper.stop()
    video.stop()
    track.stop()
    ultrasonicreader.stop()
    GPIO.cleanup()
    print("cleaned up")

movement = TankMovement.TankMovement()
ultraSonicMover = Servos.UltrasonicServo()
cameraHorizontal = Servos.CameraHorizontalServo()
cameraVertical = Servos.CameraVerticalServo()
buzzer = Buzzer.Buzzer()

led = LED.LED()

# Start streaming video
videoStreamer = VideoStreamer.VideoStreamer('tcp://*:5555')

# Start streaming Ultrasonic sensor values
ultrasonicStreamer = Streamer.Streamer('tcp://*:6666')
ultrasonic = Ultrasonic.Ultrasonic(ultrasonicStreamer)

infraredStreamer = Streamer.Streamer('tcp://*:7777')
trackSensor = TrackSensor.TrackSensor(infraredStreamer)

movementStream = movementComms.MovementComms('tcp://192.168.1.16:9999', movement, cameraVertical, cameraHorizontal, ultraSonicMover, led)

trackSensor.start()
ultrasonic.start()
videoStreamer.start()
movementStream.start()

atexit.register(cleanup, ultraSonicMover, cameraHorizontal, cameraVertical, led, buzzer, videoStreamer, trackSensor, movementStream, ultrasonic)

print("All started")
buzzer.Buzz()
time.sleep(0.5)
buzzer.stop()

k=input("press close to exit") 


 
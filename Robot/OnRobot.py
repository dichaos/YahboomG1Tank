import GPIOs.TankMovement as TankMovement
import GPIOs.Servos as Servos
import GPIOs.LEDs as LED
import GPIOs.Beeper as Beeper
import GPIOs.Ultrasonic as Ultrasonic
import GPIOs.TrackSensor as TrackSensor
import VideoStreamer
import Streamer
import time
import atexit


def cleanup(servo1, servo2, servo3, led, beeper, video, track):
    servo1.stop()
    servo2.stop()
    servo3.stop()
    led.TurnOff()
    beeper.stop()
    video.stop()
    track.stop()
    print("cleaned up")

movement = TankMovement.TankMovement()
ultraSonic = Servos.UltrasonicServo()
cameraHorizontal = Servos.CameraHorizontalServo()
cameraVertical = Servos.CameraVerticalServo()
beeper = Beeper.Beeper()

led = LED.LED()

# Start streaming video
videoStreamer = VideoStreamer.VideoStreamer('tcp://192.168.1.16:5555')

# Start streaming Ultrasonic sensor values
ultrasonicStreamer = Streamer.Streamer('tcp://192.168.1.16:6666')
ultrasonic = Ultrasonic.Ultrasonic(ultrasonicStreamer)


infraredStreamer = Streamer.Streamer('tcp://192.168.1.16:7777')
trackSensor = TrackSensor.TrackSensor(infraredStreamer)

trackSensor.start()
ultrasonic.start()
videoStreamer.start()

atexit.register(cleanup, ultraSonic, cameraHorizontal, cameraVertical, led, beeper, videoStreamer, trackSensor)

print("All started")
k=input("press close to exit") 



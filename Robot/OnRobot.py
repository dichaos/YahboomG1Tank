import GPIOs.Servos as Servos
import GPIOs.LEDs as LED
import GPIOs.Buzzer as Buzzer
import GPIOs.Ultrasonic as Ultrasonic
import GPIOs.TrackSensor as TrackSensor
import time
import atexit
import RPi.GPIO as GPIO
import Comms.MovementComms as movementComms
import Comms.Streamer as Streamer
import MicrophoneRecorder as Microphone
import VideoRecorder as Video
import GPIOs.TankMovement as TankMovement

def cleanup(servo1, servo2, servo3, led, beeper, video, track, movement, ultrasonicreader, microphoneRecorder):
    movement.stop()
    servo1.stop()
    servo2.stop()
    servo3.stop()
    led.TurnOff()
    beeper.stop()
    video.stop()
    track.stop()
    microphoneRecorder.stop()
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
videoStreamer = Streamer.Streamer('tcp://*:5555')
audioStreamer = Streamer.Streamer('tcp://*:5556')
microphoneRecorder = Microphone.MicrophoneRecorder(audioStreamer)
videoRecorder = Video.VideoRecorder(videoStreamer, cameraHorizontal, cameraVertical)

# Start streaming Ultrasonic sensor values
ultrasonicStreamer = Streamer.Streamer('tcp://*:6666')
ultrasonic = Ultrasonic.Ultrasonic(ultrasonicStreamer)

infraredStreamer = Streamer.Streamer('tcp://*:7777')
trackSensor = TrackSensor.TrackSensor(infraredStreamer)

movementStream = movementComms.MovementComms('tcp://*:9999', movement, cameraVertical, cameraHorizontal, ultraSonicMover, led, buzzer)

trackSensor.start()
ultrasonic.start()
movementStream.start()
microphoneRecorder.start()
videoRecorder.start()


atexit.register(cleanup, ultraSonicMover, cameraHorizontal, cameraVertical, led, buzzer, videoRecorder, trackSensor, movementStream, ultrasonic, microphoneRecorder)

print("All started")
buzzer.Buzz()
time.sleep(0.5)
buzzer.stop()

k=input("press close to exit") 


 
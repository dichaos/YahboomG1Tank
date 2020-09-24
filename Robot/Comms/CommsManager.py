import socket
import sys
import base64
import traceback
import threading
import numpy as np
import socketserver

class CommsManager(socketserver.StreamRequestHandler):
    def __init__(self, movement, cameraVertical, cameraHorizontal, ultrasonicMovement, led, buzzer, trackSensor, ultrasonicSensor, videoRecorder, audioRecorder):
        self.movement = movement
        self.cameraVertical = cameraVertical
        self.cameraHorizontal = cameraHorizontal
        self.ultrasonicMovement = ultrasonicMovement
        self.led = led
        self.buzzer = buzzer

        self.trackSensor = trackSensor
        self.ultrasonicSensor = ultrasonicSensor
        self.videoRecorder = videoRecorder
        self.audioRecorder = audioRecorder

    def handle(self):
        client = f'{self.client_address} on {threading.currentThread().getName()}'
        print(f'Connected: {client}')

        #I need to use the IP to send udp packets
        self.trackSensor.SetIp(self.client_address)
        self.ultrasonicSensor.SetIp(self.client_address)
        self.videoRecorder.SetIp(self.client_address)
        self.audioRecorder.SetIp(self.client_address)

        while True:
            data = self.rfile.readline()
            if not data:
                break
            self.Process(data)

        print(f'Closed: {client}')
        
    def Process(self, frame):
        if frame=="Move Stopped":
            self.movement.Stop()
        elif frame=="Move Forward":
            self.movement.Forward()
        elif frame=="Move Backwards":
            self.movement.Backwards()
        elif frame=="Turn Left":
            self.movement.TurnLeft()
        elif frame=="Turn Right":
            self.movement.TurnRight()
        elif frame.startswith('CameraLeftRight'):
            self.cameraHorizontal.Set(float(frame.split(":")[1]))
        elif frame.startswith('CameraUpDown'):
            self.cameraVertical.Set(float(frame.split(":")[1]))
        elif frame.startswith('Ultra:'):
            self.ultrasonicMovement.Set(float(frame.split(":")[1]))
        elif frame.startswith('Color:'):
            colors = frame.split(":")[1]
            self.led.SetRGB(int(colors.split(",")[0]),int(colors.split(",")[1]),int(colors.split(",")[2]))
        elif frame=="BuzzOn":
            self.buzzer.Buzz()
        elif frame=="BuzzOff":
            self.buzzer.stop()
        elif frame.startswith('Speed:'):
            self.movement.SetSpeed(int(frame.split(":")[1]))
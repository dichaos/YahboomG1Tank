import socket
import zmq
import base64
import traceback
import threading
import numpy as np

class MovementComms:
    def __init__(self, url, movement, cameraVertical, cameraHorizontal, ultrasonicMovement, led, buzzer):
        self.movement = movement
        self.cameraVertical = cameraVertical
        self.cameraHorizontal = cameraHorizontal
        self.ultrasonicMovement = ultrasonicMovement
        self.led = led
        self.buzzer = buzzer

        self.context = zmq.Context()
        self.sock = self.context.socket(zmq.PAIR)
        self.sock.bind(url)
        
        self.loop = 1
        
    def Loop(self):
        while self.loop == 1:
            try:
                frame = self.sock.recv_string()

                #print(frame)

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

            except Exception as e:
                traceback.print_exc()
                print(e)
                break

    def start(self):
        thread = threading.Thread(target=self.Loop)
        thread.daemon = True       
        thread.start() 

    def stop(self):
        self.loop = 0
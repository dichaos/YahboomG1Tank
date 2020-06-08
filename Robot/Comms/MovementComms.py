import socket
import zmq
import base64
import traceback
import threading
import numpy as np

class MovementComms:
    def __init__(self, url, movement, cameraVertical, cameraHorizontal, ultrasonicMovement):
        self.movement = movement
        self.cameraVertical = cameraVertical
        self.cameraHorizontal = cameraHorizontal
        self.ultrasonicMovement = ultrasonicMovement

        self.context = zmq.Context()
        self.sock = self.context.socket(zmq.PAIR)
        self.sock.connect(url)
        #self.sock.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))
        
        self.loop = 1
        
    def Loop(self):
        while self.loop == 1:
            try:
                frame = self.sock.recv_string()

                print(frame)

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
                    self.cameraHorizontal.Set(int(frame.split(":")[1]))
                elif frame.startswith('CameraUpDown'):
                    self.cameraVertical.Set(int(frame.split(":")[1]))
                elif frame.startswith('Ultra:'):
                    self.ultrasonicMovement.Set(int(frame.split(":")[1]))
            
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
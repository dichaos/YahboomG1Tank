import socket
import zmq
import base64
import traceback
import threading
import numpy as np

class MovementComms:
    def __init__(self, url, movement):
        self.movement = movement

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
                elif frame=="LeftMotor Forward":
                    print('not done')
                    #Left motor only forward
                elif frame=="LeftMotor Backwards":
                    print('not done')
                    #Left motor only backward
                elif frame=="RightMotor Forward":
                    print('not done')
                    #Right motor only forward
                elif frame=="RightMotor Backwards":
                    print('not done')
                    #Right motor only backward
                elif frame.startswith('Speed'):
                    self.movement.SetSpeed(50)
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
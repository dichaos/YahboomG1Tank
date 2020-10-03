import sys
import socketserver
import Comms.UDPSender as UDPServer
import GPIOs.Buzzer as Buzzer
import GPIOs.LEDs as LEDs
import GPIOs.Servos as Servos
import GPIOs.TankMovement as TankMovement
import GPIOs.TrackSensor as TrackSensor
import GPIOs.Ultrasonic as Ultrasonic
import Recorders.MicrophoneRecorder as MicrophoneRecorder
import Recorders.VideoRecorder as VideoRecorder
import traceback

buzzer = Buzzer.Buzzer()
led = LEDs.LEDs()
ultrasonicMovement = Servos.CameraVerticalServo()
cameraHorizontal = Servos.CameraHorizontalServo()
cameraVertical = Servos.UltrasonicServo()
movement = TankMovement.TankMovement()
trackSensor = TrackSensor.TrackSensor(2001)
ultrasonicSensor = Ultrasonic.Ultrasonic(2000)
videoRecorder = VideoRecorder.VideoRecorder(2002)
audioRecorder = MicrophoneRecorder.MicrophoneRecorder(2003)

def Cleanup():
    buzzer.stop()
    led.TurnOff()
    ultrasonicMovement.stop()
    cameraHorizontal.stop()
    cameraVertical.stop()
    movement.stop()
    
def Start():
    
    ultrasonicSensor.start()
    videoRecorder.start()
    audioRecorder.start()
    trackSensor.start()

def Process(frame):
    print(frame)
    try:
        if frame==b"Move Stopped":
            movement.stop()
        elif frame==b"Move Forward":
            movement.Forward()
        elif frame==b"Move Backwards":
            movement.Backwards()
        elif frame==b"Turn Left":
            movement.TurnLeft()
        elif frame==b"Turn Right":
            movement.TurnRight()
        elif frame.startswith(b'CameraLeftRight'):
            cameraHorizontal.Set(float(frame.split(b":")[1]))
        elif frame.startswith(b'CameraUpDown'):
            cameraVertical.Set(float(frame.split(b":")[1]))
        elif frame.startswith(b'Ultra:'):
            ultrasonicMovement.Set(float(frame.split(b":")[1]))
        elif frame.startswith(b'Color:'):
            colors = frame.split(b":")[1]
            led.SetRGB(int(colors.split(b",")[0]),int(colors.split(b",")[1]),int(colors.split(b",")[2]))
        elif frame==b"BuzzOn":
            buzzer.Buzz()
        elif frame==b"BuzzOff":
            buzzer.stop()
        elif frame.startswith(b'Speed:'):
            movement.SetSpeed(int(frame.split(b":")[1]))
    except Exception as e:
        traceback.print_exc()
        print(e)

class CommsManager(socketserver.StreamRequestHandler):
    def handle(self):
        
        #I need to use the IP to send udp packets
        trackSensor.SetIp(self.client_address[0])
        ultrasonicSensor.SetIp(self.client_address[0])
        videoRecorder.SetIp(self.client_address[0])
        audioRecorder.SetIp(self.client_address[0])

        Start()

        while True:
            try:
                data = self.rfile.readline()
                
                if not data:
                    break

                Process(data.strip())
            except ConnectionResetError as cre:
                break
            
        print(f'Closed: {self.client_address[0]}')
        
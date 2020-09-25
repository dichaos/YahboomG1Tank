import RPi.GPIO as GPIO

class TankMovement():
    def __init__(self):
        self.motor1 = MotorControl(16, 20, 21)
        self.motor2 = MotorControl(13, 19, 26)

    def SetSpeed(self, speed):
        self.motor1.SetSpeed(speed)
        self.motor2.SetSpeed(speed)

    def Forward(self):
        self.motor1.Forward()
        self.motor2.Forward()

    def Backwards(self):
        self.motor1.Backward()
        self.motor2.Backward()
    
    def TurnLeft(self):
        self.motor1.Forward()
        self.motor2.Backward()

    def TurnRight(self):
        self.motor1.Backward()
        self.motor2.Forward()

    def stop(self):
        self.motor1.Stop()
        self.motor2.Stop()

class MotorControl:
    def __init__(self, ENA, IN1, IN2):
        self.ENA = ENA
        self.IN1 = IN1
        self.IN2 = IN2

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)

        self.pwm_ENA = GPIO.PWM(ENA, 2000) #2000hz frequency
        self.pwm_ENA.start(50)
        
    def Forward(self):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)

    def Backward(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)

    def Stop(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)

    def SetSpeed(self, speed):
        if speed < 0:
            speed = 0
        if speed > 100: 
            speed = 100

        self.pwm_ENA.ChangeDutyCycle(speed)
import pigpio

class LEDs:
    def __init__(self):
        self.LED_R = 22
        self.LED_G = 27
        self.LED_B = 24

        self.pig = pigpio.pi()
        self.pig.set_mode(self.LED_R, pigpio.OUTPUT)
        self.pig.set_mode(self.LED_G, pigpio.OUTPUT)
        self.pig.set_mode(self.LED_B, pigpio.OUTPUT)
    
    def SetRGB(self, red, green, blue):
        pulseRed = (red * (2500-500))/255
        pulseGreen = (green * (2500-500))/255
        pulseBlue = (blue * (2500-500))/255

        if pulseRed > 0 and pulseRed < 500:
            pulseRed = 500
        elif pulseRed > 2500:
            pulseRed = 2500

        if pulseGreen > 0 and pulseGreen < 500:
            pulseGreen = 500
        elif pulseGreen > 2500:
            pulseGreen = 2500

        if pulseBlue > 0 and pulseBlue < 500:
            pulseBlue = 500
        elif pulseBlue > 2500:
            pulseBlue = 2500

        self.pig.set_servo_pulsewidth(self.LED_R, pulseRed)
        self.pig.set_servo_pulsewidth(self.LED_G, pulseGreen)
        self.pig.set_servo_pulsewidth(self.LED_B, pulseBlue)

    def TurnOff(self):
        self.pig.set_servo_pulsewidth(self.LED_R, 0)
        self.pig.set_servo_pulsewidth(self.LED_G, 0)
        self.pig.set_servo_pulsewidth(self.LED_B, 0)


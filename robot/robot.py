import RPi.GPIO as GPIO
import robotMotors as motor

#Disable the warnings from an improper shutdown
GPIO.setwarnings(False)

class robot():
    def __init__(self):
        self.rightF = motor.motorB
        self.rightB = motor.motorB_
        self.leftF = motor.motorA
        self.leftB = motor.motorA_

        #Setting up GPIO pins
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.rightF, GPIO.OUT)
        GPIO.setup(self.rightB, GPIO.OUT)
        GPIO.setup(self.leftF, GPIO.OUT)
        GPIO.setup(self.leftB, GPIO.OUT)

    def forward(self):
        GPIO.output(self.rightF, 1)
        GPIO.output(self.leftF, 1)
    def backward(self):
        GPIO.output(self.rightB, 1)
        GPIO.output(self.leftB, 1)
    def left(self):
        GPIO.output(self.rightF, 1)
        GPIO.output(self.leftB, 1)
    def right(self):
        GPIO.output(self.leftF, 1)
        GPIO.output(self.rightB, 1)

    def stop(self):
        GPIO.output(self.rightF, 0)
        GPIO.output(self.rightB, 0)
        GPIO.output(self.leftF, 0)
        GPIO.output(self.leftB, 0)
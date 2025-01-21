from gpiozero import AngularServo, Motor
from time import sleep

import math

# run with: GPIOZERO_PIN_FACTORY=lgpio python3 basics.py

try:
    servo = AngularServo(17, min_angle=-30, max_angle=50)
    _servo = True
except Exception:
    print("No servo!")
    _servo = False

try:
    motor = Motor(27, 22)
    _motor = True
except Exception:
    print("No motor!")
    _motor = False


if _motor:
    motor.forward()
if _servo:
    servo.min()


while True:

    
    servo.angle += 5.0
    for i in range(servo.min_angle, servo.max_angle):
        servo.angle = i
    
        sleep(0.1)



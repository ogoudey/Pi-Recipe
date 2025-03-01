from gpiozero import Motor
from time import sleep

import math

# run with: GPIOZERO_PIN_FACTORY=lgpio python3 basics.py


motor_bl = Motor(17, 27)
motor_fl = Motor(22, 23)
motor_br = Motor(24, 25)
motor_fr = Motor(5, 6)


def test_motors():
    motor_bl.forward()
    sleep(1)
    motor_bl.stop()
    motor_fl.forward()
    sleep(1)
    motor_fl.stop()
    motor_br.forward()
    sleep(1)
    motor_br.stop()
    motor_fr.forward()
    sleep(1)
    motor_fr.stop()
    
test_motors()


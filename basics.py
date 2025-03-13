from gpiozero import Motor
from time import sleep

import math

# run with: GPIOZERO_PIN_FACTORY=lgpio python3 basics.py
class MyMotor:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.motor = Motor(num1, num2)
        pass
    def forward(self):
        print("motor with pin ", str(self.num1), str(self.num2), "forward")
    def backward(self):
        print("motor with pin ", str(self.num1), str(self.num2), "backward")
    def stop(self):
        print("motor with pin ", str(self.num1), str(self.num2), "stopping")

motor_bl = MyMotor(17, 27)
motor_fl = MyMotor(22, 23)
motor_br = MyMotor(24, 25)
motor_fr = MyMotor(5, 6)



def test_motor(char):
    if char == "q":
        motor_bl.forward()
    elif char == "a":
        motor_bl.stop()
    elif char == "z":
        motor_bl.backward()
    elif char == "w":
        motor_fl.forward()
    elif char == "s":
        motor_fl.stop()
    elif char == "x":
        motor_fl.backward()
    if char == "e":
        motor_br.forward()
    elif char == "d":
        motor_br.stop()
    elif char == "c":
        motor_br.backward() 
    elif char == "r":
        motor_fr.forward()
    elif char == "f":
        motor_fr.stop()
    elif char == "v":
        motor_fr.backward()  

while True:
    char = input("Type a char: ")
    test_motor(char)
 

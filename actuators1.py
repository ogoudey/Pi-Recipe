from gpiozero import PWMOutputDevice, Servo

import time




cw1 = PWMOutputDevice(12)
ccw1 = PWMOutputDevice(13)

cw2 = PWMOutputDevice(18)
ccw2 = PWMOutputDevice(19)

servo = Servo(4)

def up():    
    cw1.value = 0.5
    time.sleep(0.1)
    cw1.value = 0.0
    
def down():
    ccw1.value = 0.5
    time.sleep(0.1)
    ccw1.value = 0.0

def up2():    
    cw2.value = 0.5
    time.sleep(0.1)
    cw2.value = 0.0
    
def down2():
    ccw2.value = 0.5
    time.sleep(0.1)
    ccw2.value = 0.0

def right():
    servo.min()

def left():
    servo.max()

def main():
    up()
    down()

if __name__ == "__main__":
    main()

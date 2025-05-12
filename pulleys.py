from gpiozero import PWMOutputDevice

import time




cw = PWMOutputDevice(12)
ccw = PWMOutputDevice(13)


    
def up():    
    cw.value = 0.5
    time.sleep(0.1)
    cw.value = 0.0
    
def down():
    ccw.value = 0.5
    time.sleep(0.1)
    ccw.value = 0.0


def main():
    up()
    down()

if __name__ == "__main__":
    main()

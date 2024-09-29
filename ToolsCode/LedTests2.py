import cv2
import RPi.GPIO as GPIO
from picamera2 import Picamera2
from time import sleep
from threading import Thread
import numpy as np

def takeSample():
    while True:
        takeAPicture()

def takeAPicture():
    brightness_range = [0, 25, 50, 75, 100]
    PWM_chosen = [PWM1, PWM2]
    chosen = 0
    while True:
        chosen = ~chosen
        for index in range(len(brightness_range)):
            print("LED" + str(chosen) + ": " + str(brightness_range[index]))
            PWM_chosen[chosen].ChangeDutyCycle(brightness_range[index])
            sleep(0.01)
            for frame in range(10):
                frame = picam2.capture_array()
                print(np.mean(frame))
        PWM_chosen[chosen].start(0)

if __name__ == "__main__":
    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (300, 300)}))
    picam2.start()

    # configuring pinout
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    pinoLED1 = 12
    pinoLED2 = 32
    GPIO.setup(pinoLED1, GPIO.OUT)
    GPIO.setup(pinoLED2, GPIO.OUT)

    PWM1 = GPIO.PWM(pinoLED1, 1000)
    PWM2 = GPIO.PWM(pinoLED2, 1000)
    PWM1.start(0)
    PWM2.start(0)

    t1 = Thread(target=takeSample)

    t1.start()

    t1.join()

    GPIO.cleanup()
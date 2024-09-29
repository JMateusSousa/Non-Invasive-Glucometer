import cv2
import RPi.GPIO as GPIO
from picamera2 import Picamera2
import time
import numpy as np


def take_an_sample():
    GPIO.output(pinoLED1, True)
    GPIO.output(pinoLED2, False)
    time.sleep(1)
    take_a_picture(10, "LED 1")
    GPIO.output(pinoLED1, False)
    GPIO.output(pinoLED2, True)
    time.sleep(1)
    take_a_picture(10, "LED 2")
    while True:
        i = 1

def take_a_picture(number_of_samples, text):
    for index in range(0, number_of_samples, 1):
        frame = picam2.capture_array()
        cv2.imshow("Taking Pictures", frame)
        print(text, index, np.mean(frame))
    #cv2.destroyAllWindows()
    print("=========================================")


if __name__ == "__main__":
    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (300, 300)}))
    picam2.start()

    # configuring pinout
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    pinoLED1 = 8
    pinoLED2 = 10
    GPIO.setup(pinoLED1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(pinoLED2, GPIO.OUT, initial=GPIO.LOW)

    take_an_sample()

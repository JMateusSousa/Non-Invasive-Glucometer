import cv2
import RPi.GPIO as GPIO
from picamera2 import Picamera2
import time
from threading import Thread
import numpy as np

def takeSample():
    while True:
        GPIO.output(pinoLED1, True)
        GPIO.output(pinoLED2, False)
        #takeAPicture()
        time.sleep(1)
        GPIO.output(pinoLED1, False)
        GPIO.output(pinoLED2, True)
        #takeAPicture()
        time.sleep(1)

def takeAPicture():
    while True:
        frame = picam2.capture_array()

        #_, frame = cam.read()
        cv2.imshow("Taking Pictures", frame)
        print(np.mean(frame))

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":

    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (300, 300)}))
    picam2.start()
    
    # configuring cam
    #cam = cv2.VideoCapture(0)
    #cv2.namedWindow("Taking Pictures")

    # configuring pinout
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    pinoLED1 = 12
    pinoLED2 = 10
    GPIO.setup(pinoLED1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(pinoLED2, GPIO.OUT, initial=GPIO.LOW)

    # config threads
    t1 = Thread(target=takeSample)
    t2 = Thread(target=takeAPicture)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
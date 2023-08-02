import cv2
import RPi.GPIO as GPIO
import time
import threading

def pisca():
    while (1):
        GPIO.output(pinoLED, True)
        time.sleep(0.5)
        GPIO.output(pinoLED, False)
        time.sleep(0.5)

def grava():
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Taking Pictures", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break

    cam.release()
    cv2.destroyAllWindows()


cam = cv2.VideoCapture(0)
cv2.namedWindow("Taking Pictures")

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
pinoLED = 12
GPIO.setup(pinoLED, GPIO.OUT)
pisca = threading.Thread(pisca())
grava = threading.Thread(grava())
grava.start()
pisca.start()


import cv2 as cv2
import numpy as np


def getGrayImageByFileName(fileName):
    image = cv2.imread(fileName)
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


imageZero = getGrayImageByFileName('../Resources/frame0.jpg')
imageOne = getGrayImageByFileName('../Resources/frame1.jpg')
imageTwo = getGrayImageByFileName('../Resources/frame2.jpg')

print(np.mean(imageZero))
print(np.mean(imageOne))
print(np.mean(imageTwo))

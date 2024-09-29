import cv2 as cv2
import numpy as np


def getGrayImageByFileName(fileName):
    image = cv2.imread(fileName)
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


imageZero = getGrayImageByFileName('../ToolsCode/Resources/frame0.jpg')
imageOne = getGrayImageByFileName('../ToolsCode/Resources/frame1.jpg')
imageTwo = getGrayImageByFileName('../ToolsCode/Resources/frame2.jpg')

print(np.mean(imageZero))
print(np.mean(imageOne))
print(np.mean(imageTwo))

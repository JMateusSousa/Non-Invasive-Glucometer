import os, psutil 
import numpy as np 
import cv2

print(cv2.__version__)

environmentLight = cv2.imread('../Resources/frame0.jpg')
cv2.imshow("environmentLight: %d" % np.mean(environmentLight), environmentLight)

sourceLight = cv2.imread('../Resources/frame1.jpg')
cv2.imshow("sourceLight: %d" % np.mean(sourceLight), sourceLight)

resultImage = cv2.subtract(sourceLight, environmentLight)
resultImage = cv2.cvtColor(resultImage, cv2.COLOR_BGR2GRAY)
resultImage = cv2.GaussianBlur(resultImage, (3, 3), 0)

cv2.imshow("resultado: %d" % np.mean(resultImage), resultImage)

# Get the process used memory
print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)

cv2.waitKey(0)

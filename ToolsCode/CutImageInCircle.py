import cv2
import numpy as np

# get image
sourceLight = cv2.imread("Resources/frame1.jpg")
cv2.imshow("sourceLight: %d" % np.mean(sourceLight), sourceLight)

# get image dimensions
height, weight = sourceLight.shape[:2]

# create mask
radius = 100
mask = np.zeros_like(sourceLight)
mask = cv2.circle(mask, (height//2, weight//2), radius, (255, 255, 255), -1)

#
finalImage = cv2.bitwise_and(sourceLight, mask)

cv2.imshow("Final Image: %d" % np.mean(finalImage), finalImage)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

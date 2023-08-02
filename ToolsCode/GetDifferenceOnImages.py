import cv2
import numpy as np
import matplotlib.pyplot as plt

imageOneOriginal = cv2.imread('Resources/frame2.jpg')
imageOne = cv2.cvtColor(imageOneOriginal, cv2.COLOR_BGR2GRAY)
h, w = imageOne.shape

imageTwoOriginal = cv2.imread('Resources/frame1.jpg')
imageTwo = cv2.cvtColor(imageTwoOriginal, cv2.COLOR_BGR2GRAY)


def error(img1, img2):
    diff = cv2.subtract(img1, img2)
    err = np.sum(diff ** 2)
    mse = err / (float(h * w))
    msre = np.sqrt(mse)
    return mse, diff


# match_error12, diff12 = error(imageOne, imageTwo)
# print("Image matching Error between image 1 and image 2:", match_error12)

resultedImage = cv2.subtract(imageOne, imageTwo)
print(np.mean(resultedImage))
plt.subplot(221), plt.imshow(resultedImage, 'gray'), plt.title("image1 - Image2"), plt.axis('off')
plt.subplot(222), plt.imshow(imageOneOriginal), plt.title("image1"), plt.axis('off')
plt.subplot(223), plt.imshow(imageTwoOriginal), plt.title("image2"), plt.axis('off')
plt.show()

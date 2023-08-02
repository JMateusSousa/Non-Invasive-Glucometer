import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("Taking Pictures")

img_counter = 0
images = []

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Taking Pictures", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imshow(img_name, frame)
        images.append(frame)
        print("{} written!".format(img_name))
        img_counter += 1
        if img_counter == 2:
            print("OK")
            finalImage = cv2.subtract(images[0], images[1])
            cv2.imshow("final image", finalImage)

cam.release()

cv2.destroyAllWindows()
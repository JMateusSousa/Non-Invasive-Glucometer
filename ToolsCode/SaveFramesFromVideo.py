import numpy as np
import cv2

cap = cv2.VideoCapture("Resources/ir_light.mp4")
count = 0

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (400, 400))
    print("Valor médio dos pixels do frame:", np.mean(gray))

    # Display the resulting frame
    cv2.imshow('frame', gray)

    # To save the frame
    if cv2.waitKey(0) & 0xFF == ord('s'):
        cv2.imwrite("frame%d.jpg" % count, gray)
    # To finish the system
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    count += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

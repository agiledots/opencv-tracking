import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    threshs = [
        # cv2.THRESH_BINARY,
        cv2.THRESH_BINARY_INV,
        # cv2.THRESH_TRUNC,
        # cv2.THRESH_TOZERO,
        # cv2.THRESH_TOZERO_INV
    ]

    for index, thresh in enumerate(threshs):
        ret, frame = cv2.threshold(frame, 127, 255, thresh)

        # Display the resulting frame
        cv2.imshow('frame{}'.format(index), frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

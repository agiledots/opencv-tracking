import numpy as np
import cv2

def frame_resize(frame, n=0.5):
    return cv2.resize(frame, (int(frame.shape[1] * n), int(frame.shape[0] * n)))


cap = cv2.VideoCapture("./videos/Pacific bluefin tuna (cutter).mp4")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = frame_resize(frame)

    # cv2.imshow("Original", frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    threshs = [
        # cv2.THRESH_BINARY,
        # cv2.THRESH_BINARY_INV,
        # cv2.THRESH_TRUNC,
        # cv2.THRESH_TOZERO,
        # cv2.THRESH_TOZERO_INV
    ]


    ret, frame = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY_INV)

    # Display the resulting frame
    cv2.imshow('frame{}', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

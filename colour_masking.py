import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while 1:
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of red color in HSV
    mask1 = cv.inRange(hsv, (0, 50, 20), (5, 255, 255))
    mask2 = cv.inRange(hsv, (175, 50, 20), (180, 255, 255))
    # Merge the mask
    mask = cv.bitwise_or(mask1, mask2)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
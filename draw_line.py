import numpy as np
import math
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    img = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)

    # get average pixel value
    average = math.floor(np.average(img))

    # Draw a diagonal line with thickness of 5 px where the colour and thickness depends on the average pixel value
    cv.line(img, (0, 0), (511, 511), (average, 0, 0), math.floor(average / 2))
    # draw circle, radius changes with average pixel value
    cv.circle(img, (447, 63), average, (0, 0, 255), -1)

    cv.imshow("line", img)

    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
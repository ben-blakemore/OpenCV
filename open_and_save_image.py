import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("meme_test.jpg"))

if img is None:
    sys.exit("Could not read image")

cv.imshow("Display Window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("meme_test.png", img)

import sys

import cv2 as cv

from object_tracking.display import Display

W = 1920 // 2
H = 1080 // 2

display = Display(W, H)
orb = cv.ORB_create()

def process_frame(img):
    img = cv.resize(img, (W, H))
    kp, des = orb.detectAndCompute(img, None)
    for point in kp:
        u, v = map(lambda x: int(round(x)), point.pt)
        cv.circle(img, (u, v), color=(0, 255, 0), radius=3)
    display.draw(img)


if __name__ == "__main__":
    if sys.argv == "camera":
        cap = cv.VideoCapture(0)
    else:
        cap = cv.VideoCapture("object_tracking/dashcam.mp4")
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            process_frame(frame)
        else:
            break


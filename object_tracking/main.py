import sys
import time

import cv2 as cv
import numpy as np

from object_tracking.display import Display

W = 1920 // 2
H = 1080 // 2

logo = cv.imread('./resources/white-cross.png')
size = 50
logo = cv.resize(logo, (size, size))
img2gray = cv.cvtColor(logo, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 1, 255, cv.THRESH_BINARY)

display = Display(W, H)

class FeatureExtractor(object):
    GX = 16//2
    GY = 12//2

    def __init__(self):
        self.orb = cv.ORB_create(1000)

    def extract(self, img):
        # detect key points
        # sy = img.shape[0]//self.GY
        # sx = img.shape[1]//self.GX
        # akp = []
        # for ry in range(0, img.shape[0], sy):
        #     for rx in range(0, img.shape[1], sx):
        #         img_chunk = img[ry:ry + sy, rx:rx + sx]
        #         kp = self.orb.detect(img_chunk, None)
        #         for p in kp:
        #             p.pt = (p.pt[0] + rx, p.pt[1] + ry)
        #             akp.append(p)
        # return akp
        features = cv.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000, qualityLevel=0.1, minDistance=3)
        return features

fe = FeatureExtractor()

def process_frame(img):
    img = cv.resize(img, (W, H))
    akp = fe.extract(img)

    last_f = akp[0]
    for f in akp:
        assert f.all() == last_f.all()
        u, v = map(lambda x: int(round(x)), f[0])
        u2, v2 = map(lambda x: int(round(x)), last_f[0])
        cv.circle(img, (u, v), color=(0, 0, 255), radius=1)
        cv.line(img, (u, v), (u2, v2), color=(255, 255, 255))
        last_f = f

    display.draw(img)


if __name__ == "__main__":
    if sys.argv[1] == "camera":
        cap = cv.VideoCapture(0)
    else:
        cap = cv.VideoCapture("object_tracking/dashcam.mp4")
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            process_frame(frame)
        else:
            break

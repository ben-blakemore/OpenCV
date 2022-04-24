import cv2 as cv
import time
import math

img1 = cv.imread("resources/suez.jpg")
img2 = cv.imread("resources/icon.jpg")

print(img1.shape)
print(img2.shape)

while True:
    print(math.sin(time.time()))
    # modulates the blend of 2 images
    dst = cv.addWeighted(img1, math.fabs(math.sin(time.time())), img2, 0.3, 0)
    cv.imshow('dst', dst)
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
import cv2
import numpy as np

img = cv2.imread('1.jpg')
dst = cv2.flip(img, 0)

cv2.imshow('FlipedImg', dst)

while(True):
    key = cv2.waitKey(0)
    if key == 27:
        break
cv2.destroyAllWindows()

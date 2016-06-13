import cv2
import numpy as np

img = cv2.imread('./1.jpg')

# img(y, x)
tree = img[160:520, 540:810]
img[160:520, 60:330] = tree

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

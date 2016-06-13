import cv2
import numpy as np

img = cv2.imread('./2.jpg')

result = img[175:620, 0:620]
# cv2.imshow('toggle', result)

result[0:445, 0:67] = img[175:620, 505:572]
result[0:445, 67:140] = img[175:620, 73:146]
result[0:445, 140:215] = img[175:620, 818:893]
result[0:445, 215:315] = img[175:620, 262:362]
result[0:445, 315:386] = img[175:620, 604:675]
result[0:445, 386:472] = img[175:620, 400:486]
result[0:445, 472:552] = img[175:620, 712:790]
result[0:445, 552:620] = img[175:620, 182:250]


cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

img = cv2.imread('./2.jpg')

# part1 = img[175:620, 73:146]
# part2 = img[175:620, 182:250]
# part3 = img[175:620, 262:362]
# part4 = img[175:620, 400:486]
# part5 = img[175:620, 505:572]
# part6 = img[175:620, 604:675]
# part7 = img[175:620, 712:790]
# part8 = img[175:620, 818:893]
# cv2.imwrite('./lab03Img/part1.jpg', part1)
# cv2.imwrite('./lab03Img/part2.jpg', part2)
# cv2.imwrite('./lab03Img/part3.jpg', part3)
# cv2.imwrite('./lab03Img/part4.jpg', part4)
# cv2.imwrite('./lab03Img/part5.jpg', part5)
# cv2.imwrite('./lab03Img/part6.jpg', part6)
# cv2.imwrite('./lab03Img/part7.jpg', part7)
# cv2.imwrite('./lab03Img/part8.jpg', part8)

part1 = cv2.imread('./lab03Img/part1.jpg')
part2 = cv2.imread('./lab03Img/part2.jpg')
part3 = cv2.imread('./lab03Img/part3.jpg')
part4 = cv2.imread('./lab03Img/part4.jpg')
part5 = cv2.imread('./lab03Img/part5.jpg')
part6 = cv2.imread('./lab03Img/part6.jpg')
part7 = cv2.imread('./lab03Img/part7.jpg')
part8 = cv2.imread('./lab03Img/part8.jpg')

result = img[175:620, 0:620]
# cv2.imshow('toggle', result)

result[0:445, 0:67] = part5
result[0:445, 67:140] = part1
result[0:445, 140:215] = part8
result[0:445, 215:315] = part3
result[0:445, 315:386] = part6
result[0:445, 386:472] = part4
result[0:445, 472:552] = part7
result[0:445, 552:620] = part2


cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
from matplotlib import pyplot as plt

elephant = cv2.imread('./2.jpg')

G = elephant.copy()
gp = [G]
for i in xrange(4):
    G = cv2.pyrDown(G)
    gp.append(G)
lp = [gp[3]]
for i in xrange(3, 0, -1):
    GE = cv2.pyrUp(gp[i])
    L = cv2.subtract(gp[i - 1], GE)
    lp.append(L)
# cv2.imshow('GE', GE)

edges = cv2.Canny(elephant, 254, 255)
cv2.imshow('edges', edges)

edgesGE = cv2.Canny(GE, 254, 255)
cv2.imshow('edgesGE', edgesGE)


# ret,thresh = cv2.threshold(img,127,255,0)
# image, contours, hierarchy = cv2.findContours(thresh, 1, 2)
# cv2.imshow('image', image)
#
# cnt = contours[0]
#
# rect = cv2.minAreaRect(cnt)
# box = cv2.boxPoints(rect)
# box = np.int0(box)
# img = cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
# cv2.imshow('finall', img)

# rows, cols = edges.shape
# isElephantArea = False
# startCol = []
# endCol = []
# for c in range(cols):
#     for r in range(rows):
#         if edges[r][c] != 0 and isElephantArea == False:
#             isElephantArea = True
#             startCol.append(c)
#             break
#         isElephantArea = False
#         endCol.append(c)
#
# print(startCol[:20])
# print(endCol[:20])

def fillArea(img):
    # img to gray
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 110, 255, 0)
    # find contours
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # draw contours
    image = cv2.drawContours(image, contours, 3, (0, 255, 0), 3)
    # floodFill
    retval, floodfilled, mask, rect = cv2.floodFill(image, None, (0, 0), 255)
    return floodfilled

elephant = fillArea(elephant)
cv2.imshow('FloodFilled', elephant)

# kernel = np.ones((5, 5), np.uint8)
# dilation = cv2.dilate(elephant, kernel, iterations = 1)
# cv2.imshow('dilation', dilation)


# ret, thresh = cv2.threshold(dilation, 110, 255, 0)
# # find contours
# image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# # draw contours
# image = cv2.drawContours(image, contours, 3, (0, 255, 0), 3)
# # floodFill
# retval, floodfilled, mask, rect = cv2.floodFill(image, None, (0, 0), 255)


# img = move(img, dilation, 480, 5)
# cv2.imshow('AfterMoveDilation', elephant)

cv2.waitKey(0)
cv2.destroyAllWindows()





cv2.waitKey(0)
cv2.destroyAllWindows()

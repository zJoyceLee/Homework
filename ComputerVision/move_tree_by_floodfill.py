import cv2
import numpy as np

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

def move(img, myshape, deltaX, deltaY):
    rows, cols = myshape.shape
    for r in range(rows):
        for c in range(cols):
            if treeShape[r][c] > 1:
                img[195+r+deltaY, 540+c-deltaX] = img[195+r, 540+c]
    return img

img = cv2.imread('./1.jpg')
tree = img[190:510, 535:815]
treeShape = fillArea(tree)[5:315, 5:275]
tree = tree[5:315, 5:275]
cv2.imshow('FloodFilled', treeShape)

kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(treeShape, kernel, iterations = 1)
cv2.imshow('dilation', dilation)

img = move(img, dilation, 480, 5)
cv2.imshow('AfterMoveDilation', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

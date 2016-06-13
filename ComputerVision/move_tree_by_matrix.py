import numpy as np
import cv2

def count(lst, val):
    '''
    count 255 in row
    '''
    counter = 0
    for i in lst:
        if i >= val:
            counter += 1
    return counter

def isfill(lst, row, col, n, minNum):
    '''
    lst: edge point
    row: the row where 255 < col/4
    n: matrix(n,n)
    minNum: the minNum of 255 in the matrix
    '''
    counter = 0
    for r in range(row-n/2, row+(n+1)/2):
        counter += count(lst[r][col-n/2:col+(n+1)/2], 1)
    if counter >= minNum:
        return True
    else:
        return False


img = cv2.imread('./1.jpg')
edges = cv2.Canny(img,100,200)
# print(edges)

delta = 480

rows, cols, color = img.shape

for r in range(rows):
    counter255 = count(edges[r], 255)

    if counter255 != 0 and (counter255 < cols / 4):
        for c in range(0,cols-1):
            if isfill(edges, r, c, 9, 2):
                img[r][c-delta] = img[r][c]


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

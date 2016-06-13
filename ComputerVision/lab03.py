import cv2
import numpy as np

def pyramid(img):
    # generate Gaussian pyramid
    G = img.copy()
    gp = [G]
    for i in xrange(6):
        G = cv2.pyrDown(G)
        row, col, channel = G.shape
        print('%d: %d, %d, %d' % (i, row, col, channel))
        gp.append(G)

    # generate Laplacion Pyramid
    lp = [gp[5]]
    for i in xrange(5, 0, -1):
        GE = cv2.pyrUp(gp[i])
        row, col, channel = GE.shape
        print('%d: %d, %d, %d' % (i, row, col, channel))
        L = cv2.subtract(gp[i-1], GE)
        lp.append(L)

    return lp

img1 = cv2.imread('./lab03Img/part5.jpg')
img2 = cv2.imread('./lab03Img/part1.jpg')
# img1 = cv2.imread('1.jpg')
# img2 = cv2.imread('2.jpg')

lp1 = pyramid(img2)
lp2 = pyramid(img2)

LS = []
for la, lb in zip(lp1, lp2):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols/2], lb[:, cols/2:]))
    LS.append(ls)

ls_ = LS[0]
for i in xrange(1, 6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

# real = np.hstack((la[:, :cols/2], lb[:, :cols/2]))
cv2.imwrite('./lab03Img/Pyramid_blending2.jpg', ls_)

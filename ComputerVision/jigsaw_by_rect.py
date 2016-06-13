import cv2
import numpy as np

def pyramid(img):
    # generate Gaussian pyramid
    G = img.copy()
    gp = [G]
    for i in xrange(6):
        G = cv2.pyrDown(G)
        gp.append(G)

    # generate Laplacion Pyramid
    lp = [gp[5]]
    for i in xrange(5, 0, -1):
        GE = cv2.pyrUp(gp[i])
        L = cv2.subtract(gp[i-1], GE)
        lp.append(L)

    return lp

img = cv2.imread('./2.jpg')
taskImg = img.copy()

def divide(img):
    #1, 2, 3, 4, 5, 6, 7, 8
    #5, 1, 8, 3, 6, 4, 7, 2
    # part1 = img[170:620, 60:170]
    # part2 = img[170:620, 170:255]
    # part3 = img[170:620, 255:385]
    # part4 = img[170:620, 385:500]
    # part5 = img[170:620, 500:580]
    # part6 = img[170:620, 580:680]
    # part7 = img[170:620, 680:800]
    # part8 = img[170:620, 800:900]

    part1 = img[172:620, 0:128]
    part2 = img[172:620, 70:230]
    part3 = img[172:620, 255:385]
    part4 = img[172:620, 385:500]
    part5 = img[172:620, 500:628]
    part6 = img[172:620, 580:680]
    part7 = img[172:620, 680:800]
    part8 = img[172:620, 800:900]

    cv2.imwrite('./lab03Img/part1.jpg', part1)
    cv2.imwrite('./lab03Img/part2.jpg', part2)
    cv2.imwrite('./lab03Img/part3.jpg', part3)
    cv2.imwrite('./lab03Img/part4.jpg', part4)
    cv2.imwrite('./lab03Img/part5.jpg', part5)
    cv2.imwrite('./lab03Img/part6.jpg', part6)
    cv2.imwrite('./lab03Img/part7.jpg', part7)
    cv2.imwrite('./lab03Img/part8.jpg', part8)

divide(img)



img1 = cv2.imread('./lab03Img/part1.jpg')
img2 = cv2.imread('./lab03Img/part2.jpg')
img3 = cv2.imread('./lab03Img/part3.jpg')
img4 = cv2.imread('./lab03Img/part4.jpg')
img5 = cv2.imread('./lab03Img/part5.jpg')
img6 = cv2.imread('./lab03Img/part6.jpg')
img7 = cv2.imread('./lab03Img/part7.jpg')
img8 = cv2.imread('./lab03Img/part8.jpg')


lp1 = pyramid(img5)
lp2 = pyramid(img1)

LS = []
for la, lb in zip(lp1, lp2):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols/2], lb[:, cols/2:]))
    LS.append(ls)

ls_ = LS[0]
for i in xrange(1, 6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

real = np.hstack((la[:, :cols/2], lb[:, :cols/2]))
cv2.imwrite('./lab03Img/Pyramid_blending2.jpg', ls_)
# cv2.imwrite('Direct_blending.jpg', real)


# taskImg[175:620, 60:140] = img[175:620, 500:580]
# taskImg[175:620, 140:250] = img[175:620, 60:170]
# taskImg[175:620, 250:350] = img[175:620, 800:900]
# taskImg[175:620, 350:480] = img[175:620, 255:385]
# taskImg[175:620, 480:580] = img[175:620, 580:680]
# taskImg[175:620, 580:695] = img[175:620, 385:500]
# taskImg[175:620, 695:815] = img[175:620, 680:800]
# taskImg[175:620, 815:900] = img[175:620, 170:255]
#
# cv2.imshow('taskImg', taskImg)
# cv2.imwrite('./lab03Img/taskImg.jpg', taskImg)


cv2.waitKey(0)
cv2.destroyAllWindows()

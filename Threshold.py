from cv2 import THRESH_BINARY, THRESH_BINARY_INV, THRESH_TOZERO, THRESH_TOZERO_INV, THRESH_TRUNC
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# while(1):
img= cv.imread("gradient.png",0)

_,tv1=cv.threshold(img,127,255,THRESH_BINARY)
_,tv2=cv.threshold(img,127,255,THRESH_BINARY_INV)
_,tv3=cv.threshold(img,50,255,THRESH_TRUNC)
_,tv4=cv.threshold(img,50,255,THRESH_TOZERO)
_,tv5=cv.threshold(img,50,255,THRESH_TOZERO_INV)


titles= ["img","binary","binary_inv","trunc","tozero","tozero_inv"]
image= [img,tv1,tv2,tv3,tv4,tv5]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(image[i],"gray")
    plt.title(titles[i])
    
    # k= cv.waitKey(1) & 0xFF

    # if k == 27:
    #     break

# cv.imshow("tv1",tv1)
# cv.imshow("image",img)
# cv.imshow("tv2",tv2)
# cv.imshow("tv3",tv3)
# cv.imshow("tv4",tv4)
# cv.imshow("tv5",tv5)


plt.show()
cv.waitKey(0)
cv.destroyAllWindows


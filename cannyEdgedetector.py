from operator import truediv
from cv2 import getTrackbarPos
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def nothing(x):
    pass    
    

cv.namedWindow("cannyw")
cv.createTrackbar("th1","cannyw",0,255,nothing)
cv.createTrackbar("th2","cannyw",0,255,nothing)

while(True):
    img= cv.imread("messi5.jpg",cv.IMREAD_GRAYSCALE)
    th1= getTrackbarPos("th1","cannyw")
    th2= getTrackbarPos("th2","cannyw")
    edges= cv.Canny(img,th1,th2)
    cv.imshow("cannyEdgedetection",edges)
    k= cv.waitKey(1) & 0xFF 
    if k == 27:
        break

cv.destroyAllWindows()

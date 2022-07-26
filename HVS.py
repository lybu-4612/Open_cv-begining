import numpy as np 
import cv2 as cv

def nothing(x):
    pass

cv.namedWindow("track")

cv.createTrackbar("LH","track",0,255,nothing)
cv.createTrackbar("LS","track",0,255,nothing)
cv.createTrackbar("LV","track",0,255,nothing)
cv.createTrackbar("UH","track",255,255,nothing)
cv.createTrackbar("US","track",255,255,nothing)
cv.createTrackbar("UV","track",255,255,nothing)

while(True):    
    
    frame= cv.imread("smarties.png")
    
    hsv= cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
    lh=cv.getTrackbarPos("LH","track")
    ls=cv.getTrackbarPos("LS","track")
    lv=cv.getTrackbarPos("LV","track")
    uh=cv.getTrackbarPos("UH","track")
    us=cv.getTrackbarPos("US","track")
    uv=cv.getTrackbarPos("UV","track")

    
    l_b= np.array([lh,ls,lv])
    U_b= np.array([uh,us,uv])
    
    mask= cv.inRange(hsv,l_b,U_b)
    res= cv.bitwise_and(frame,frame,mask=mask)
    
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    
    cv.imshow("frame",frame)
    cv.imshow("mask",mask)
    cv.imshow("result",res)

cv.destroyAllWindows()
        

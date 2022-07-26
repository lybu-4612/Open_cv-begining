import numpy as np
import cv2

img1= np.zeros((250,500,3),np.uint8)
img2= cv2.imread("image_1.png")
img1= cv2.rectangle(img1,(200,0),(300,100),(255,0,0),-1)

img3= cv2.bitwise_or(img2,img1)

cv2.imshow("image1",img1)
cv2.imshow("image2",img2)
cv2.imshow("image3",img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
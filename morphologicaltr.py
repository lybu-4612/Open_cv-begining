import numpy as np 
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread("smarties.png", cv.IMREAD_GRAYSCALE) 
_,mask= cv.threshold(img,220,255,cv.THRESH_BINARY_INV)

kernel=np.ones((2,2),np.uint8)
dlt= cv.dilate(mask,kernel,iterations=2)
eroded= cv.erode(mask,kernel,iterations=2)
opening= cv.morphologyEx(mask,cv.MORPH_OPEN,kernel)
closing= cv.morphologyEx(mask,cv.MORPH_CLOSE,kernel)
images= [img,mask,dlt,eroded,opening,closing]
titles= ["image","mask","dilate","eroded","opening","closing"]

for i in range(6):
    plt.subplot(3,3,i+1),plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
    
plt.show()
    
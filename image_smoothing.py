import  numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("opencv-logo-white.png")
kernel= np.ones((5,5),np.float32)/25
filtr= cv.filter2D(img,-1,kernel)
blur1= cv.blur(img,(5,5))
blur2= cv.GaussianBlur(img,(5,5),0)
median_blur= cv.medianBlur(img,5)
bilateral= cv.bilateralFilter(img,9,76,76)

img= [img,filtr,blur1,blur2,median_blur,bilateral]
titles= ["Image", "filter","blur1","GaussianBlur","median_blur","bilateral"]

for i in range(6):
    plt.subplot(3,3,i+1),plt.imshow(img[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
    
plt.show()
import numpy as np

import cv2

img= cv2.imread("lena.jpg",-1)
# img= np.zeros([512,512,3], dtype=np.uint8)

img= cv2.line(img,(0,255),(255,255),(0,255,0),20)
img= cv2.arrowedLine(img,(0,0),(255,255),(0,0,255),20)

# img= cv2.rectangle(img,(0,220),(255,0),(0,222,123),-1)
img= cv2.circle(img,(223,23),243,(0,222,123),-1)
img= cv2.putText(img,"Hello World",(10,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow("image",img)
key= cv2.waitKey(4000)

if key == 27:
    cv2.destroyAllWindows()
elif key == ord("s"):
    cv2.imwrite("lena_copy.png",img)
    cv2.destroyAllWindows()

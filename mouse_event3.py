import numpy as np 
import cv2


def Click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue= img[x,y,0]
        green= img[x,y,1]
        red= img[x,y,2]
        
        cv2.circle(img,(x,y),3,(0,255,0),-1)
        colorimage= np.zeros((512,512,3),np.uint8)
        colorimage[:] = [blue,green,red]
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # strrgb = str(blue)+ "," +str(green)+ "," +str(red)
        # cv2.putText(colorimage,strrgb,(x,y),font,1,(0,0,255),1)
        # cv2.imshow("color", colorimage)
        
        cv2.imshow("color",colorimage)
        
img= cv2.imread("lena.jpg")
# img= np.zeros((512,512,3),np.uint8)

cv2.imshow("image",img)
cv2.setMouseCallback("image",Click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
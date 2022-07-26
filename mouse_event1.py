import numpy as np
import cv2


def Click_event(event, x, y,frame,params):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        print(x ,"," ,y)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        strxy = str(x)+ "," +str(y)
        cv2.putText(img,strxy,(x,y),frame,1,(0,255,255),2)
        cv2.imshow("image", img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue= img[y,x,0]
        green= img[y,x,1]
        red= img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strrgb = str(blue)+ "," +str(green)+ "," +str(red)
        cv2.putText(img,strrgb,(x,y),font,1,(0,0,255),1)
        cv2.imshow("image", img)
        
    
# img= np.zeros((512,512,3),np.uint8)
img= cv2.imread("lena.jpg")
cv2.imshow("image",img)

cv2.setMouseCallback("image",Click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

        
        
        
        
        
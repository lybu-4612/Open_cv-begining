import numpy as np
import cv2


def Click_event(event,x,y,frames,params):
    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))
        if  len(points) >= 2 :
            cv2.line(img,points[-1],points[-2],(0,255,0),4)
            
        cv2.imshow("image",img)
            
        
        
img= np.zeros((512,512,3),np.uint8)
cv2.imshow("image",img)

points= []
cv2.setMouseCallback("image",Click_event)


cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import datetime

cap= cv2.VideoCapture(0);

# cap.set(3,1280)
# cap.set(4,720)

# print(cap.get(3))
# print(cap.get(4))
while (cap.isOpened()):
    
    rt,frame = cap.read()
    
    if rt:
        
        font= cv2.FONT_HERSHEY_SIMPLEX
        # text= "width"  + str(cap.get(3)) +  "height"+ str(cap.get(4))
        datet= str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10,115), font, 1, (0,0,255), 2, cv2.LINE_AA)
        cv2.imshow("frame", frame)
        
        
        if cv2.waitKey(1)  & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()

        
    
    
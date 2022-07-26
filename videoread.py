import cv2


cap= cv2.VideoCapture(0);
fourcc= cv2.VideoWriter_fourcc(*'XVID')
out= cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))

while (1):
    
    ret,frame= cap.read()
    if ret == True:
        
        out.write(frame)
        # gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",frame)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
out.release()
cv2.destroyAllWindows()
    
    
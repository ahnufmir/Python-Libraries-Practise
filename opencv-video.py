import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

while cap.isOpened():
    ret, frame = cap.read()
    out.write(frame)
    # img_color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow("window", frame)
    
    if cv2.waitKey(25) & 0xFF == ord('x'):
        break

out.release()
cv2.destroyAllWindows()    
import cv2 
import numpy as np

img = cv2.imread("testingpic.jpg")

flag = False
ix = -1
iy = -1

def draw(event, x,y, flags, params):
    global flag, ix, iy

    if event == 1:
        flag = True
        ix = x
        iy = y

    # elif event == 0:
    #     if flag == True:
    #         cv2.rectangle(img, pt1=(ix,iy) , pt2= (x,y), color= (0,255,255), thickness=1 )

    elif event == 4:
        h,w,c = img.shape
        # flag = False
        fx = x
        fy = y
        cv2.rectangle(img, pt1=(ix,iy) , pt2= (x,y), color= (0,0,0), thickness=1 )

        cropped_img = img[iy:fy, ix:fx]
        cv2.imshow("new_window", cropped_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        cv2.putText(cropped_img, org= (50,50), fontScale=1, color=(0,0,0    ), fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX, lineType= cv2.LINE_AA, text= "Image Downloaded!")
        cv2.imwrite("OUTPUT PIC\cropped.jpg", cropped_img)


cv2.namedWindow(winname="window")
cv2.setMouseCallback("window" ,draw)

while True:

    cv2.imshow("window", img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()


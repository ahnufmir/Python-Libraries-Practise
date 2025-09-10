import cv2


image = cv2.imread("germany.png")

if image is not None:
    cv2.imshow("Image Editor", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image didnot load!")    


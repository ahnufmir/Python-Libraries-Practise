import cv2
import numpy as np


image = cv2.imread("germany.png")

# if image is not None:
#     cv2.imshow("Image Editor", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("Image didnot load!")    

#Picture Dimensions check

# if image is not None:
#     h,w,c = image.shape
#     print(f"Height :{h} \n Width: {w}\n Color Channel(s): {c}")
# else:
#     print("Image didnot load!")   


# Small Task for practise


print("---- Welcome to OpenCV --------")
# img_loc = input("Give me image location for which you want to convert ot grayscale: ")
# image = cv2.imread(img_loc)
# if image is not None:
#     grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     user_decision = input("Do you want to save/show image? Press y for 'save; and n for 'show'")
#     if user_decision == 'y':
#         img_loc_output = input("Give me exact location to save the image")
#         cv2.imwrite(img_loc_output, grey_img)
#     elif user_decision == 'n':
#         cv2.imshow("Image Editor", grey_img)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#     else:
#         print("Write either 'y' or 'n'")  
# else:
#     print("Picture didnot Load :(")



## IMAGE MODIFICATION
# Image Crop

# cropped_image = image[100:200,50:150]
# cv2.imshow("Image", cropped_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Image Resize
# resized_img = cv2.resize(image,(925,925))
# cv2.imshow("Image", resized_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Greycale Image
# print(image.shape)
# grey_scale_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# print(grey_scale_img.shape)

#Playing with the channels of the image
# imgBlue = image[:,:,0]
# imgGreen = image[:,:,1]
# imgRed = image[:,:,2]
# new_img = np.hstack((imgBlue,imgGreen,imgRed))
# cv2.imshow("heyyyyyyyyyyy",new_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Flipping an image
# flipped_img = cv2.flip(image, 0)
# cv2.imshow("heyyyyyyyyyyy",flipped_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Drawing Shapes

img = np.zeros((500,500,3))

cv2.rectangle(img, pt1=(100,100), pt2=(200,250), color=(0,0,255), thickness=100)
cv2.line(img, pt1=(0,0), pt2=(500,500), color=(255,0,0), thickness=100)
cv2.circle(img, center=(250,300), radius=50, color=(0,255,0), thickness=100 )
cv2.imshow("window", img)
cv2.waitKey(0)


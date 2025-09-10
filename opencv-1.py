import cv2


# image = cv2.imread("germany.png")

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
img_loc = input("Give me image location for which you want to convert ot grayscale: ")
image = cv2.imread(img_loc)
if image is not None:
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    user_decision = input("Do you want to save/show image? Press y for 'save; and n for 'show'")
    if user_decision == 'y':
        img_loc_output = input("Give me exact location to save the image")
        cv2.imwrite(img_loc_output, grey_img)
    elif user_decision == 'n':
        cv2.imshow("Image Editor", grey_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Write either 'y' or 'n'")  
else:
    print("Picture didnot Load :(")              




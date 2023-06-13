import cv2
import numpy as np
image = cv2.imread("E:\\Coding\\Python\\openCV\\tutorial\\girl.jpg")
print(image.shape)
#rESIZING THE IMAGE
resized_image =cv2.resize(image,(200,150))
print(resized_image.shape)

#CROPPING THE IMAGE
cropped_image = image[70:200,100:200] #here we used numpy array to crop
print(cropped_image.shape,"hhhh")
cv2.imshow("girl image", image)
cv2.imshow("resized", resized_image)
cv2.imshow("cropped", cropped_image)
cv2.waitKey(0)

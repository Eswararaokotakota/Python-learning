import cv2,numpy as np

image = cv2.imread("E:\\Coding\\Python\\openCV\\tutorial\\girl.jpg")

stack_hor = np.hstack((image,image,image))

stack_ver = np.vstack((image,image)) #to stack images in np   both images should nither rgb nor gray 

cv2.imshow("horizontal",stack_hor)
cv2.imshow("vertical",stack_ver)
cv2.waitKey(0)
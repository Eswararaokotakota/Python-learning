import cv2
import numpy as np

image = cv2.imread("E:\\Coding\\Python\\openCV\\tutorial\\girl.jpg")
kernal = np.ones((5,5),np.uint8) #created a 5/5 matrix kernal for dilation process

grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #displayas grey image
# cv2.namedWindow('image',cv2.WINDOW_NORMAL)
blur_image =cv2.GaussianBlur(grey_image,(7,7),0) #kernal(3,3) should be odd number

edge_detection = cv2.Canny(image,200,100) #By changing the values you can change the detection amount of edge

#now we are doing dilation(to increase the edgewidth)
img_dilation = cv2.dilate(edge_detection, kernal, iterations=1) #no iterations increases then edge width also increases

#now we will do erosion  (means decreses the width of the edge)
img_erosion = cv2.erode(img_dilation, kernal, iterations=1)

cv2.imshow("cute girl",grey_image)
cv2.imshow("blur image",blur_image)
cv2.imshow("edge image",edge_detection)
cv2.imshow("dilation image",img_dilation)
cv2.imshow("erosion image",img_erosion)
cv2.waitKey(0)

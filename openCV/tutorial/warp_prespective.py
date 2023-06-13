
import cv2,numpy as np

image = cv2.imread("E:\\Coding\\Python\\openCV\\tutorial\\cards.jpg")

width,height = 500,700

points= np.float32([[493,87],[905,243],[289,635],[663,794]]) #writing the points of card to warp
#above points [width,height] [left top corner],[right top corner],[left bottom corner],[right bottom corner]points

tell_pos = np.float32([[0,0],[width,0],[0,height],[width,height]]) #telling the points given above points to place where [left,top][right,top][left,bottom][right,bottom]

matrix = cv2.getPerspectiveTransform(points,tell_pos)  #creating the matrix for image

out_image =cv2.warpPerspective(image,matrix,(width,height)) #applying the warpprespective 

cv2.imshow("jaf",image)
cv2.imshow("warped card",out_image)
cv2.waitKey(0)
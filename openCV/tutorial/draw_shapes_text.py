import cv2, numpy as np

# cv2.imread("E:\\Coding\\Python\\openCV\\tutorial\\girl.jpg")
#now we will create an image
# image = np.zeros((512,512)) #this is 2d image
image = np.zeros((512,512,3),np.uint8) #a 3dimage means a color image
# image[:] = 255,0,0 #[:] means it willapply to the whole image blue color(255,0,0)
print(image.shape)

cv2.line(image,(0,0),(300,300),(0,255,20),5)#image,(startingpoint),(ending point),(color),(thickness)
cv2.line(image,(0,0),(image.shape[1],image.shape[0]),(0,255,20),2) #Will draw a line from left top corner to rigth bottom corner
cv2.rectangle(image,(0,0),(250,400),(255,0,0),3)#remove,3 and you can write cv2.FILLED to fill the rectangle #draws a rectangle in the image
cv2.circle(image,(400,100),50,(255,0,255),2) #(image,(center point),radius,(color),thickness)
cv2.putText(image,"Hello!",(350,200),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(250,255,0),1) # (image,text,(position),font,text size,(color),thickness)

cv2.imshow("Drawings on image",image)
cv2.waitKey(0)
import cv2



img = cv2.imread("E:\Coding\Python\openCV\camera.jpg",0)#"0" representing the image in grey scale

# cv2.resize(img[100,100])
cv2.imshow("Title: camera.jpg",img)

cv2.waitKey(0)#waits infinatly till any key pressed

cv2.destroyAllWindows()
#image will be displayed

cv2.imwrite("E:\Coding\Python\openCV\saved_images\greycam.jpg",img) #will saves the grey colored image in to this directory
print("----------------Photo Saved!----------------")
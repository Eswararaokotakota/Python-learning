#Load and show an image and when i press a perticular key it should close 
#pip install opencv-python
# import cv2


# image = cv2.imread('nature.jpg')
# window_name = 'image'
# cv2.imshow(window_name,image)
# cv2.waitKey(100)
  
# #closing all open windows 
# cv2.destroyAllWindows() 

import cv2 
  
# path 
path = r'E:\\Coding\\Python\\Tasks\\Task_7\\nature.jpg'
  
# Reading an image in default mode
image = cv2.imread(path)
  
# Window name in which image is displayed
window_name = 'nature'
 # the image and the dimensions
# resize = cv2.resize(image, (800, 800)) 
# Using cv2.imshow() method 
# Displaying the image 
cv2.imshow(window_name)
  
#waits for user to press any key 
#(this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0) 
  
#closing all open windows 
cv2.destroyAllWindows()
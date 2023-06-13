import cv2
import numpy as np
import os 


random_bytes = bytearray(os.urandom(750000)) 
nparray = np.array(random_bytes)
green_img = nparray.reshape(500, 500, 3) 

green_img[:,:] = [0,255,0]
cv2.imshow("[0,255,0]", green_img)
cv2.waitKey(0)

white_img = green_img
white_img[:,:]= [255,255,255]
cv2.imshow("[255,255,255]", white_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("task5 completed..!")
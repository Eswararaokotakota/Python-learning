from cv2 import imshow
import numpy as np
import cv2
import os

path = "E:\\Coding\\Python\openCV\\saved_images\\created_with_numpy\\"

random_byte_array = bytearray(os.urandom(1200000))
flatNumpyArray = np.array(random_byte_array)

grayimage = flatNumpyArray.reshape(3000,400)
cv2.imwrite(path+"grayImage.png",grayimage)
print("Process done! Image saved in the directory")
cv2.imwrite(r"C:\Users\Eswar\Desktop\3d_rim_work\image.jpg",grayimage)
cv2.imshow("Grey Image",grayimage)
cv2.waitKey(200)
cv2.destroyAllWindows()


#now we can convert the image to color
colorImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite(path+"colorImage.png",colorImage)
print("Color image also saved")
cv2.imshow("Randome Color Image", colorImage)
cv2.waitKey(200)
cv2.destroyAllWindows()


#making grey box in random-grey image
play_img = flatNumpyArray.reshape(300,400)
play_img[10:50,150:250] = [223]
cv2.imwrite(path+"Play_gray_img.png",play_img)
cv2.imshow("white Line",play_img)
cv2.waitKey(200)
cv2.destroyAllWindows()


random_bytes = bytearray(os.urandom(1350000)) 
nparray = np.array(random_bytes)
play_color_img = nparray.reshape(500, 900, 3) #we should give the correct value to the reshape function which is the output by multiplying them 500x900x3 = 1350000
#making color image box in random-colored image
play_color_img[125:350,225:675] = [51,225,100]
play_color_img[350:450,225:675] = [100,50,100]
play_color_img[0:124,225:675] = [100,50,100]
cv2.imwrite(path+"play_color_img.png",play_color_img)
cv2.imshow("color img play",play_color_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Done!.....")

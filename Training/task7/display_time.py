import datetime
import cv2
import numpy as np
import time


# date_time = datetime.datetime.now()
# print(date_time)

camera = cv2.VideoCapture(0)

# return_value, image = camera.read()
# cv2.imwrite('E:\\Coding\\Python\\Training\\task7\\live.jpg', image)


def creating_image():
    count = 0
    while True:
        # time.sleep(1)
        # white = np.zeros((300, 300, 3), np.uint8)
        # white[:,:] = [255,255,255]
        date_time = datetime.datetime.now()
        return_value, image = camera.read()
        count+=1
        dt = str(date_time)+str(count)
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(image,str(date_time),(50,20),font,0.5,(0,0,255),1)
        cv2.imwrite('E:\\Coding\\Python\\Training\\task7\\'+str(count)+'.jpg', image)
        print(date_time)
        cv2.imshow("green.jpg",image)
        if cv2.waitKey(1) & 0xFF == ord("x"): 
            break
creating_image()




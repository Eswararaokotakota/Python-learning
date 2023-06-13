import cv2
import numpy as np




def empty(a):
    pass

# img_path = "E:\\Coding\\Python\\openCV\\tutorial\\car.jpg"

video = cv2.VideoCapture(0)# 0 will read the default webcamera

video.set(3,640) #3 means the height of the display to show
video.set(4,480) #4 means the width
video.set(10,10)#10 means the brightness parameter

while True:
    success, image = video.read()
    # cv2.imshow("press 'z' to exit", image)
    if cv2.waitKey(1) & 0xFF == ord("z"): #waits untill pressing the z key
        break

    #creating a trackbar
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars",640,240)
    cv2.createTrackbar("Hue min","TrackBars",0,179,empty) #The hue in open cv is 179 only(normal hue range is 360)
    cv2.createTrackbar("Hue max","TrackBars",78,179,empty)
    cv2.createTrackbar("Sat min","TrackBars",51,255,empty)
    cv2.createTrackbar("Sat max","TrackBars",255,255,empty)
    cv2.createTrackbar("Val min","TrackBars",174,255,empty)
    cv2.createTrackbar("Val max","TrackBars",255,255,empty)
    while True:
        # img = cv2.imread(img_path)
        hsv_img = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

        #getting the trackbars positions
        #here we are reading the values of trackbar and applying them on a mask to select the color 
        h_min = cv2.getTrackbarPos("Hue min","TrackBars")
        h_max = cv2.getTrackbarPos("Hue max","TrackBars")
        s_min = cv2.getTrackbarPos("Sat min","TrackBars")
        s_max = cv2.getTrackbarPos("Sat max","TrackBars")
        v_min = cv2.getTrackbarPos("Val min","TrackBars")
        v_max = cv2.getTrackbarPos("Val max","TrackBars")
        print(h_min,h_max,s_min,s_max,v_min,v_max)

        #now we are creating a masks 
        #imported the numpy
        lower = np.array([h_min,s_min,v_min])
        upper = np.array([h_max,s_max,v_max])
        mask = cv2.inRange(hsv_img,lower,upper)  #the image and the limits for the mask lower and upper
        #creates a image whith black and white values which is a mask to select the color range with the trackbars

        #now we are applying this mask on the original image and getting the original image parts from the mask
        result_img = cv2.bitwise_and(image,image,mask=mask) #checks the images and when both images values are true it will store that
        #above original image and original image and mask=mask that we have created with the trackbars
        cv2.imshow("car",image)
        cv2.imshow("hsv car",hsv_img)
        cv2.imshow("mask",mask)
        cv2.imshow("result",result_img) #grabs the mask from original image and shows it   WORKING NICE! WELL

        cv2.imwrite("E:\\Coding\\Python\\openCV\\tutorial\\color_detection.jpg",result_img)

        cv2.waitKey(1)

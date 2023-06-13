import cv2

video = cv2.VideoCapture(0)# 0 will read the default webcamera

video.set(3,640) #3 means the height of the display to show
video.set(4,480) #4 means the width
video.set(10,10)#10 means the brightness parameter

while True:
    success, image = video.read()
    cv2.imshow("press 'z' to exit", image)
    if cv2.waitKey(1) & 0xFF == ord("z"): #waits untill pressing the z key
        break
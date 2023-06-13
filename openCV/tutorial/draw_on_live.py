import cv2

#taking the code from we webcam_video to show the camera

video = cv2.VideoCapture(0)# 0 will read the default webcamera

video.set(3,640) #3 means the height of the display to show
video.set(4,480) #4 means the width
video.set(10,10)#10 means the brightness parameter

mycolor = []

#now we are getting the some of the code from the color_detection.py to here for find our color
def find_color(img):
    # hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # lower = np.array([h_min,s_min,v_min])
    # upper = np.array([h_max,s_max,v_max])
    # mask = cv2.inRange(hsv_img,lower,upper)
    # cv2.imshow("image",mask)

while True:
    success, footage = video.read()
    cv2.imshow("press 'z' to exit", image)
    if cv2.waitKey(1) & 0xFF == ord("z"): #waits untill pressing the z key
        break

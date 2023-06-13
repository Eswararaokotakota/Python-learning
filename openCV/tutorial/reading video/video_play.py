import cv2
import time

video =cv2.VideoCapture("E:\\Coding\\Python\\openCV\\reading video\\cool_nature.mp4")
video.set(3,640) #width
video.set(4,480) #height
print("Playing video..... \n Press 'z' to close the video")

time.sleep(1)

while True:
    success,img = video.read()
    cv2.imshow("Press 'z' to exit",img)
    if cv2.waitKey(1) & 0xFF == ord("z"):
        break
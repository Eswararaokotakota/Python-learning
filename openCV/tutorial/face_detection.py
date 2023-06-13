import cv2

#For face detection there is some raw methonds to detect the faces by training the meching and creating a cascade file (.xml file)
#here open cv has already has some default cascades to detect numberplates faces objects etc
#we are using he open cv provided cascade file to detect the face in th image
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread("E:\\Coding\\Python\\openCV\\tutorial\\girl.jpg")

grey_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(grey_image,1.1,4)

#creating a boundry box to draw the rectangle on face
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)


#therer are more cascades available in online or you can create your own 

#bokka avvatlaaaaaaaaaaaaaa

cv2.imshow("Result", img)
cv2.waitKey(0)
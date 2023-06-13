import cv2

#we will detect the contures and the edges and we will say which shape is the shape

def getcontours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #retr_external is the best one for detecting the contours
    for cnt in contours:
        area = cv2.contourArea(cnt) #will get the values of the contoures
        print(area)
        #now we will draw the contoures
        # cv2.drawContours(imgContour,cnt,-1,(255,0,0),3) # for the loop it will draw the every value in the original image which imgcontoure
        #now we will add min values for detection so it will not introduces the noise
        if area>10: #if it is minimum(0) then it will detects every contoure value so noise may occur and increasing toomuch will may cause
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            #drawing the corners of the shapes
            parameters = cv2.arcLength(cnt,True)
            # print(parameters)
            #getting the approximate corner points so we can say the object later based on these values
            approx = cv2.approxPolyDP(cnt,0.02*parameters,True)
            # print(approx) #bit it will give matrix values 
            #now we will get lenth of them hence we can directly get the no of corners
            # print(len(approx))
            objcor = len(approx)
            x, y, w, h = cv2.boundingRect(approx) #to draw the bounding box border 
            
            if objcor ==3: objectType = "Triangle"
            elif objcor==4:
                asptratio = w/float(h)
                if asptratio >0.95 and asptratio<1.05: objectType="Square"
                else: objectType="Rectangle"
            elif objcor>4: objectType="Circle"
            else: objectType = "none"
            #now we will draw that
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(255,0,255),2)
            cv2.putText(imgContour,objectType,  
                        (x+(w//2)-50,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
            

            

path = "E:\\Coding\\Python\\openCV\\tutorial\\shapes.png"

img = cv2.imread(path)
imgContour = img.copy() #copying the original image and using it in draw function above
#converting it to gray
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#applying the blur
blur_img = cv2.GaussianBlur(gray_img,(7,7),1)
#now we will do edge detection
edge_img = cv2.Canny(blur_img,50,50)#50 50 thrishold values

getcontours(edge_img)#calling the function which detects the edges(contoures)

# cv2.imshow("Original", img)
# cv2.imshow("gray image", gray_img)
# cv2.imshow("blur image", blur_img)
# cv2.imshow("edge image", edge_img)
cv2.imshow("Detected contoures", imgContour)

cv2.waitKey(0)
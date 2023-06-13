import cv2
img = cv2.imread("E:\Coding\Python\openCV\camera.jpg")

cv2.imshow("camera", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# i=0
# for i in range(10):
#     cv2.imwrite("E:\Coding\Python\openCV\saved_images\multiple_images\"camerass"+str(i)+".jpg", img)
#     i+=1
#     print(i,"images saved")

print("-----------------saved-----------------")

for i in range(10):
    cv2.imwrite("E:\Coding\Python\openCV\saved_images\multiple_images\camera"+str(i)+".jpg", img)
    print(i,"images saved")

print("-----------------saved-----------------")
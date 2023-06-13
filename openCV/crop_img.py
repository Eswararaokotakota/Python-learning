import cv2

img = cv2.imread("E:\Coding\Python\openCV\camera.jpg")

rows, columns,_ = img.shape

print("rows", rows)
print("columns", columns)

imgage = img[0:100, 0:150] #[height:height, width:width]

cv2.imshow("asdas",imgage)
cv2.waitKey(0)
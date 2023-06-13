import cv2


img1=-cv2.imread("E:\\Coding\\Python\\Training\\task_4\\turtle.jpg")
img2=cv2.imread("E:\\Coding\\Python\\Training\\task_4\\banana.jpg")

v_concat = cv2.vconcat([img1,img1])

h_concat = cv2.hconcat([img2,img2])

cv2.imshow("Vertical",v_concat)
cv2.waitKey(0)
cv2.imshow("Horizontal",h_concat)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Task4 completed...!")
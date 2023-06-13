import cv2

img1 =cv2.imread("C:\\Users\\Eswar\\Desktop\\image_stitching\\bangalore\\des_left_gamma_crp.jpg")
img2 =cv2.imread( "C:\\Users\\Eswar\\Desktop\\image_stitching\\bangalore\\des_right_gamma_crp.jpg")
# img3 =cv2.imread("E:\Coding\Python\openCV\saved_images\multiple_images\camera3.jpg")

print("hello")
concatinated = cv2.vconcat([img1,img2]) #vertically
h_concat = cv2.hconcat([img1,img2])
cv2.imshow("V-concatinated",concatinated)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("H-concatinated",h_concat)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("C:\\Users\\Eswar\\Desktop\\image_stitching\\bangalore\\des_hconcat.jpg", h_concat)
print("Done!....")
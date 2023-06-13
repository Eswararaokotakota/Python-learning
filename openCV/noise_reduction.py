import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Eswar\\Desktop\\sample_noise.jpg")
out_path = "C:\\Users\\Eswar\\Desktop\\noiss.jpg"

print(img.shape)
#rESIZING THE IMAGE
# resized_image =cv2.resize(img,(512,385))
# print(resized_image.shape)
# denoise_3 = cv2.fastNlMeansDenoisingColored(img,None,3,3,7,21)


def denoise():
    denoise = cv2.fastNlMeansDenoisingColored(img,None,3,3,7,21)
    print("function executed")
    # crop = cv2.sharpening[0:1540,100:2048] #height and width
    # cv2.imshow("denoise image", denoise)
    # cv2.waitKey(0)
    cv2.imwrite(out_path,denoise)
    print("denoise executed")


def blur_methods(self):
    blur_img = cv2.blur(img,(5,5))

    gaussian_blur = cv2.GaussianBlur(img, (7,7), 2)

    median_blur = cv2.medianBlur(img, 5)

    bilateral_blur = cv2.bilateralFilter(img, 9, 75, 75)

    sharpening = cv2.addWeighted(bilateral_blur, 1.6, gaussian_blur, -0.5, 0)

        # crop = sharpening[0:1540,100:2048] #height and width

    
def warp_cutting(self):

    width,height = 1508,1040

    points= np.float32([[570,507],[1520,500],[0,1000],[1700,1260]]) #writing the points of card to warp
        #above points [width,height] [left top corner],[right top corner],[left bottom corner],[right bottom corner]points
    tell_pos = np.float32([[0,0],[width,0],[0,height],[width,height]]) #telling the points given above points to place where [left,top][right,top][left,bottom][right,bottom]

    matrix = cv2.getPerspectiveTransform(points,tell_pos)  #creating the matrix for image

        # out_image =cv2.warpPerspective(crop,matrix,(width,height)) #applying the warpprespective 

# cv2.imshow("original",resized_image)
# # cv2.imshow("blur",blur_img)
# # cv2.imshow("median blur", median_blur)
# cv2.imshow("gaussian blur", gaussian_blur)
# cv2.imshow("bilateral blur", cv2.resize(bilateral_blur,(1024,770)))
# cv2.imshow("Sharpening", cv2.resize(sharpening,(1024,770)))
# cv2.imshow("cropped", crop)
# cv2.imshow("wrapped", out_image)
# cv2.imshow("denoise", denoise_3)

# cv2.imwrite("E:\\Coding\\Python\\openCV\\noisy_img1a2000.jpg",crop)
# cv2.imwrite("E:\\Coding\\Python\\openCV\\noisy_img1adfwrap2000.jpg",out_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Done!")

denoise()
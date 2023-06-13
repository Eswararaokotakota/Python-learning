
import cv2
import numpy as np

# input_img_path = r'D:\Night_HAWK\Data\ex_5K\2022_06_17_kajaguda__To__mountainroad_Lane3_LHS\Asset\Asset1\2022_06_17_22_10_34_568461_Asset1.jpg'
# output_img_path = r'D:\Night_HAWK\Data\ex_5K\converted\assest_1_2.6gamma1.jpg'
input_img_path = "E:\\Coding\\Python\\openCV\\gamma_correction\\sample_images\\b.jpg"

output_img_path = "E:\\Coding\\Python\\openCV\\gamma_correction\\sample_images\\bb.jpg"


def gammaCorrection(src, gamma):
    invGamma = 1 / gamma
 
    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)
 
    return cv2.LUT(src, table)
 


img = cv2.imread (input_img_path)
print(img.shape)
# crp_img = img[700:1300,100:2048]
gammaImg = gammaCorrection(img, 2.6)
denoise = cv2.fastNlMeansDenoisingColored(gammaImg,None,3,3,7,21)
#crop


# cv2.imshow('Original image', img)
# cv2.imshow('Gamma corrected image', gammaImg)
# cv2.waitKey(2000)
# cv2.destroyAllWindows()

cv2.imwrite(output_img_path,gammaImg)
print("--------image saved-------")
print("--------Done!--------")
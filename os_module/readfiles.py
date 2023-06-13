import os
import cv2
import numpy as np
import time

def gammaCorrection(src, gamma):
   
#gamma correction equation 
    invGamma = 1 / gamma
    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)
    return cv2.LUT(src, table)

#paths for reading images and writing them after process
output_img_path = r'E:\\Coding\\Python\\openCV\\gamma_correction\\converted\\'
img_path= r'E:\\Coding\\Python\\openCV\\gamma_correction\\sample_images'

#Path checking
in_path_check = os.path.isdir(img_path)
out_path_check = os.path.isdir(output_img_path)
if (in_path_check):
    print("Input path correct")
    if(out_path_check):
        print("Output path also correct.")
        print("Processing the images....")
        for i in range(1,4):
             print(i)
             time.sleep(0.5) #just for fun counting 3 numbers 1 2 3.....

# If paths are correct then executing the gamma correction on images in the folder
        img_list = os.listdir(img_path)
        #print(img_list)
        for filename in img_list:
            print(filename)
   
            #reading image
            img = cv2.imread (os.path.join(img_path,filename))

                #applying gamma function
            gammaImg = gammaCorrection(img, 2.6)

            #saving images
            cv2.imwrite(output_img_path+filename+".jpg",gammaImg)
            print("--------image saved-------")# Working well!
    else:
        print(str(output_img_path)+"---Entered output path is incorrect! Please verify : )")
    
else:
    print(str(img_path)+"---Entered input path is not exists! Please verify :)")
    
 
#Code working successfully :)

cv2.imshow('Original image', img)
cv2.imshow('Gamma corrected image', gammaImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

 


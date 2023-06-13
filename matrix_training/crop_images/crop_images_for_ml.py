import cv2
import os

input_folder_path = "E:\\Coding\\Python\\openCV\\saved_images\\multiple_images\\"
output_images_path = "E:\\Coding\\Python\\openCV\\saved_images\\multiple_images\\croped_images"

if not os.path.exists(output_images_path):
    os.mkdir(output_images_path)

img_list = os.listdir(input_folder_path)

for i in img_list:
    img= cv2.imread(os.path.join(input_folder_path,i))
    # img = cv2.imread(i)
    # print(img.shape)
    height, width, _ = img.shape
    
    # height = int(height/2)
    width2 = int(width/2)
    
    crp_img1 = img[0:height, 0:width2]
    crp_img2 = img[0:height, width2:width]
    i = i.replace('.jpg',"_")
    out_path = os.path.join(output_images_path+"//",i)
    
    cv2.imwrite(out_path+"1.jpg", crp_img1)
    cv2.imwrite(out_path+"2.jpg", crp_img2)

    print(i)
    # print(img.shape)
    
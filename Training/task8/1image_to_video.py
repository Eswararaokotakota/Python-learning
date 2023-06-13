import cv2
import os
import numpy as np

folder_path = "E:\\Coding\\Python\\Training\\task8\\captured_images_task7\\"
if not os.path.exists:
    folder_path = os.mkdir("E:\\Coding\\Python\\Training\\task8\\captured_images_task7")

def create_images():
    for i in range(255):
        image = np.zeros((300, 300, 3), np.uint8)
        image[:,:] = [0,0,i]
        cv2.imwrite(folder_path+"red"+str(i)+".jpg",image)
        if i == 254:
            for j in range(255):
                image = np.zeros((300, 300, 3), np.uint8)
                image[:,:] = [0,j,0]
                cv2.imwrite(folder_path+"green"+str(j)+".jpg",image)
            if j == 254:
                for k in range(255):
                    image = np.zeros((300, 300, 3), np.uint8)
                    image[:,:] = [k,0,0]
                    cv2.imwrite(folder_path+"blue"+str(k)+".jpg",image)
    print("Generated images...!")

def make_video():

    images_path = folder_path
    out_path = "E:\\Coding\\Python\\Training\\task8\\"
    video_name = "img_to_video.mp4"
    video_path = out_path+video_name
    img_list = []

    images = os.listdir(images_path)
    # print(images)
    for i in images:
        i = folder_path+i
        # print(i)
        img_list.append(i)
    # print(img_list)   
    frame = cv2.imread(img_list[0])
    size = list(frame.shape)
    del size[2]
    print(size)
    size.reverse()

    format = cv2.VideoWriter_fourcc(*'mp4v')
    video =cv2.VideoWriter(video_path,format,30,size) #video path , video format, fps, size

    for i in range(len(img_list)):
        video.write(cv2.imread(img_list[i]))

    video.release() 
    print("Video created")  

# create_images()
make_video()
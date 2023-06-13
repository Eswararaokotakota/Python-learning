#DATA AUGUMENTATION
#Here we are doing the image manipulations like rotation, flipping, blurring so on... and saving them superately in a specific folder

import pandas as pd
import cv2
import ast
import numpy as np
import os
import csv
from pathlib import Path
import tqdm

input_csv_path = r"Y:\LCMS_Data_21-12-22\model_1\labled_data_for_ml.csv"
path = r"Y:\LCMS_Data_21-12-22\model_1\Augumentation"
if not os.path.exists(path):
    os.mkdir(path)

csv_file_path = os.path.join(path+"/"+"augumentation.csv")
if not os.path.exists(csv_file_path):
    with open(csv_file_path, "w", newline="") as csv_file:
        # csv_file = csv.reader(csv_file)
        writer = csv.writer(csv_file)
        writer.writerow(["filename","width", "height","class", "xmin", "ymin", "xmax", "ymax"])

out_images_path = os.path.join(path+"/"+"images")      
if not os.path.exists(out_images_path):
    os.mkdir(out_images_path)


def rotate_c():
    rotate_c = cv2.rotate(resized_img, cv2.ROTATE_90_CLOCKWISE)
    x1 = y11 
    x2 = y22
    y1 = x11
    y2 = x22
    # print("Rotated_90_clk",x1,y1,x2,y2)
    h = rotate_c.shape[0]
    w = rotate_c.shape[1]
    image = os.path.join(out_images_path+"/"+b+"rotate90c.jpg")
    cv2.imwrite(image,rotate_c)
    image_name1 = a+"rotate90c.jpg"
    # print(image_name1)
    with open (csv_file_path,"a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([image_name1,w,h,distress_class, x1,y1,x2,y2])
    
    
def rotate_ac(): #90 degrees anti clockwise
    rotate_ac = cv2.rotate(resized_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    x1 = y11
    x2 = y22
    y1 = width-x22
    y2 = width-x11
    h = rotate_ac.shape[0]
    w = rotate_ac.shape[1]
    image = os.path.join(out_images_path+"/"+b+"rotate90ac.jpg")
    cv2.imwrite(image,rotate_ac)
    image_name1 = a+"rotate90ac.jpg"
    with open (csv_file_path,"a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([image_name1,w,h,distress_class, x1,y1,x2,y2])
    
def rotate_c_180(): #180 degrees clockwise
    rotate_180_c = cv2.rotate(resized_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    x1 = width-x22
    x2 = width-x11
    y1 = height-y22
    y2 = height-y11
    h = rotate_180_c.shape[0]
    w = rotate_180_c.shape[1]
    image_name1 = a+"rotate_180_c.jpg"
    image = os.path.join(out_images_path+"/"+b+"rotate_180_c.jpg")
    cv2.imwrite(image,rotate_180_c)
    with open (csv_file_path,"a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([image_name1,w,h,distress_class, x1,y1,x2,y2])
    
def flip_hor():
    flip_h = cv2.flip(resized_img,1)
    x1 = width-x22
    x2 = width-x11
    y1 = y11
    y2 = y22
    image = os.path.join(out_images_path+"/"+b+"flip_h.jpg")
    h = flip_h.shape[0]
    w = flip_h.shape[1]
    cv2.imwrite(image,flip_h)
    image_name1 = a+"flip_h.jpg"
    with open (csv_file_path,"a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([image_name1,w,h,distress_class, x1,y1,x2,y2])
    

def flip_ver():
    flip_v = cv2.flip(resized_img,0)
    x1 = x11
    x2 = x22
    y1 = height-y22
    y2 = height-y11
    image = os.path.join(out_images_path+"/"+b+"flip_v.jpg")
    h = flip_v.shape[0]
    w = flip_v.shape[1]
    cv2.imwrite(image,flip_v)
    image_name1 = a+"flip_v.jpg"
    with open (csv_file_path,"a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([image_name1,w,h,distress_class, x1,y1,x2,y2])


def blur1():
    ksize = (10,1)
    blur_img1 = cv2.blur(resized_img,ksize)
    image = os.path.join(out_images_path+"/"+b+"blur1.jpg")
    h = blur_img1.shape[0]
    w = blur_img1.shape[1]
    cv2.imwrite(image,blur_img1)
    image_name1 = a+"blur1.jpg"
    with open (csv_file_path,"a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([image_name1,w,h,distress_class, x11,y11,x22,y22])
    
def blur2():
    ksize = (5,5)
    blur_img2 = cv2.blur(resized_img,ksize)
    image = os.path.join(out_images_path+"/"+b+"blur2.jpg")
    h = blur_img2.shape[0]
    w = blur_img2.shape[1]
    cv2.imwrite(image,blur_img2)
    image_name1 = a+"blur2.jpg"
    with open (csv_file_path,"a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([image_name1,w,h,distress_class, x11,y11,x22,y22])
    
def brightness():
    brightnes_img = cv2.convertScaleAbs(resized_img, resized_img, 1, 120)
    image = os.path.join(out_images_path+"/"+b+"brightnes_img.jpg")
    h = brightnes_img.shape[0]
    w = brightnes_img.shape[1]
    cv2.imwrite(image,brightnes_img)
    image_name1 = a+"brightnes_img.jpg"
    with open (csv_file_path,"a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([image_name1,w,h,distress_class, x11,y11,x22,y22])
        
df = pd.read_csv(input_csv_path)
print(df.info())
files = df["File_Path"]
# print(files.shape)
boundingbox = df["BoundingBox"]
dclass = df["Distress_Class"]
# Id = df["Id"]
# print(Id[1])
count = 0       
for i in files:
    image = cv2.imread(i)
    resized_img = cv2.resize(image,(1565,132))
    bounding_box1 = boundingbox[count]
    distress_class = dclass[count]
    # print(count)
    # Id = Id[count]
    a = os.path.splitext(i)
    a = a[0] #image path without extension (.jpg)
    b = os.path.split(a)
    b = b[1]   # image name without extension (.jpg)
    # print(a,distress_class, resized_img.shape)    
    # cv2.imshow("reimage", resized_img)
    # cv2.waitKey(0)
    # print(bounding_box1)
    bb = ast.literal_eval(bounding_box1)
    x11 = int(bb[0])
    y11 = int(bb[1])
    x22 = int(bb[2])+int(bb[0])
    y22 = int(bb[3])+int(bb[1])
    if x11<0:
        x11 = 0
    if x22<0:
        x22 = 0
    if y11<0:
        y11=0
    if y22<0:
        y22=0
    height = resized_img.shape[0]
    width = resized_img.shape[1]
    with open (csv_file_path,"a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([i,width,height,distress_class, x11,y11,x22,y22])
    cv2.imwrite(out_images_path+"/"+b+".jpg", resized_img)
    
    if distress_class == "Pothole":
        rotate_c()
        rotate_ac()
        rotate_c_180()
        flip_hor()
        flip_ver()
        # blur1()
        # blur2()
        brightness()
    elif distress_class == "Data Loss":
        rotate_c()
        # blur2()
        flip_hor()

    elif distress_class == "Transverse Cracks":
        flip_hor()
        
    elif distress_class == "Longitudinal Cracks":
        flip_hor()

    elif distress_class == "Transverse Joint":
        flip_hor()

    # elif distress_class == "Longitudinal Joint":
    #     flip_hor()
    #     flip_ver()
    #     blur1()
    #     blur2()
    #     brightness()
    
    elif distress_class == "Manhole":
        rotate_c()
        rotate_ac()
        rotate_c_180()
        flip_hor()
        flip_ver()
        # blur1()
        # blur2()
        brightness()
        
    elif distress_class == "Unclassified Cracks":
        rotate_c()
        rotate_ac()
        rotate_c_180()
        flip_hor()
        flip_ver()
        # blur1()
        # blur2()
        brightness() 
    print(count)
    count+=1
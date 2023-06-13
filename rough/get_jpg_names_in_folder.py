# import the modules
import os
import cv2
import numpy as np
import argparse

 
# get the path/directory
folder_dir = "E:\Coding\Python\openCV\saved_images\multiple_images"
for images in os.listdir(folder_dir):
 
    # check if the image ends with png
    if (images.endswith(".jpg")):
        print(images)
     
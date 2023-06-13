import cv2
import os
import shutil
import time

#read image          ----done----
#create two folders  ----done----
#save 100 copies of image in x folder  ----done----
#Copy images from x to y folder  
#Calculate the speed

path = "E:\\Coding\\Python\\Training\\task_3\\girl.jpg"
girl = cv2.imread(path)
# cv2.imshow("girl",girl)
# cv2.waitKey(0)


class task3:
    def create_folders(self):
        self.folder_x="E:\\Coding\\Python\\Training\\task_3\\X"
        self.folder_y="E:\\Coding\\Python\\Training\\task_3\\Y"
        if not os.path.exists(self.folder_x):
            os.mkdir(self.folder_x)
        if not os.path.exists(self.folder_y):
            os.mkdir(self.folder_y)
        print("Folders Created")

    def regenerate_images(self):
        for i in range(100):
            cv2.imwrite("E:\\Coding\\Python\\Training\\task_3\\X\\camera"+str(i)+".jpg", girl)
        print("100 images saved..!")

    def copy_images(self):
        start_time = time.time()
        files = os.listdir(self.folder_x)
        for image in files:
            shutil.copy2(os.path.join(self.folder_x,image), self.folder_y)
        end_time = time.time()
        ex_time = end_time - start_time
        print("Copied..!")
        files_size = 2  #MB
        speed = files_size/ex_time
        print(speed,"MB/s")

task_3 = task3()
task_3.create_folders()
task_3.regenerate_images()
task_3.copy_images()

print("Done Task3 completed..!")
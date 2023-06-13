import numpy as np
import cv2
import os 

path = "E:\\Coding\\Python\\Training\\task6\\"

class task6:
    def create_color_images(self):
        
        self.red = np.zeros((300, 300, 3), np.uint8)
        self.red[:,:] = [0,0,255]
        cv2.imwrite(path+"red.jpg",self.red)
        
        self.blue = np.zeros((300, 300, 3), np.uint8)
        self.blue[:,:] = [255,0,0]
        cv2.imwrite(path+"blue.jpg",self.blue)

        self.green = np.zeros((300, 300, 3), np.uint8)
        self.green[:,:] = [0,255,0]
        cv2.imwrite(path+"green.jpg",self.green)

        self.black = np.zeros((300, 300, 3), np.uint8)
        self.black[:,:] = [0,0,0]
        cv2.imwrite(path+"black.jpg",self.black)


    def h_concat_images(self):
        concat1 = cv2.hconcat([self.red,self.blue])
        concat2 = cv2.hconcat([self.green,self.black])
        concat = cv2.hconcat([concat1,concat2])
        cv2.imshow("h-concat", concat)
        cv2.waitKey(0)


    def v_concat_images(self):
        concat1 = cv2.vconcat([self.red,self.blue])
        concat2 = cv2.vconcat([self.green,self.black])
        concat = cv2.vconcat([concat1,concat2])
        cv2.imshow("v-conact", concat)
        cv2.waitKey(0)

task = task6()
task.create_color_images()
task.h_concat_images()
task.v_concat_images()

print("task6 completed..!")
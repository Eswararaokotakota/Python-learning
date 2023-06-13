import os
import cv2
import numpy as np
import time

start_time = time.time()

def gammaCorrection(src, gamma):
    invGamma = 1 / gamma
 
    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)
 
    return cv2.LUT(src, table)


in_path = 'E:\\Coding\\Python\\openCV\\gamma_correction\\sample_images\\2022_06_17_22_10_43_255991_Asset1.jpg'
out_path = 'E:\\Coding\\Python\\openCV\\gamma_correction\\sections_g_c\\'
image = cv2.imread(in_path)
print(image.shape)
# npImage = cv2.imread(path,mode='RGB')
nparray = np.asarray(image)
print(nparray.shape)

section_1=nparray[0:385,0:2048]
section_2=nparray[385:770,0:2048]
section_3=nparray[770:1152,0:2048]
section_4=nparray[1152:1537,0:2048]
section_last=nparray[1537:1540,0:2048]
# nparray[0:385,0:2048]
# print(section_1)

section_1_GC = gammaCorrection(section_1,2.6)
section_2_GC = gammaCorrection(section_2,2.4)
section_3_GC = gammaCorrection(section_3,2.2)
section_4_GC = gammaCorrection(section_4,2.2)
section_last_GC = gammaCorrection(section_last,2.2)

# cv2.imshow("section_1",section_1_GC)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imshow("section_1",section_2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# resize = nparray.resize(1000,1000)
# resize = cv2.resize(nparray,(1000,1000))
final = cv2.vconcat([section_1_GC,section_2_GC,section_3_GC,section_4_GC,section_last_GC])
cv2.imshow("section_1",final)
cv2.waitKey(200)
cv2.destroyAllWindows()
cv2.imwrite(out_path+"section_1.jpg",final)
print("Done!....")
#9462760

# cv2.imshow("adbhvhnfg",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
print("-----%s Seconds-----"%(time.time()-start_time))#prins the execution time of this program
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Eswar\\Desktop\\samplee.jpg")
out_path = "C:\\Users\\Eswar\\Desktop\\sample1.jpg"

alpha = 2
beta = 50

result = cv2.addWeighted(img, alpha, np.zeros(img.shape, img.dtype), 0, beta)

cv2.imwrite(out_path,result)
import cv2

path = "C:\\Users\\Eswar\\Desktop\\image_stitching\\new\\assetleftcalib.png"

img = cv2.imread(path)
print(img.shape)
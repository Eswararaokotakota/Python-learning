import cv2
import pandas as pd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import numpy as np


def plot():
    # img = cv2.imread("E:\\Coding\\Python\\matrix_training\\task-1\\data\\rotated_images\\2022_09_03_15_38_59_368731_Distress_cam1.jpg")
    # imgr = cv2.imread("E:\\Coding\\Python\\matrix_training\\task-1\\data\\rotated_images\\2022_09_03_15_38_59_368731_Distress_cam11.jpg")

    # print(img.shape)
    # print(imgr.shape)

    imgr = imgr.resize(int(imgr.shape[0]/4), int(imgr.shape[1]/4))
    s = (687* 3.4343,101* 3.4343)
    e = (265* 3.4343,325* 3.4343)
    cam1 = cv2.rectangle(imgr, pt1=(int(687*3.4343),int(101*3.4343)), pt2=(int(265*3.4343),int(325*3.4343)),color=(0,255,0),thickness=2)
    cv2.imshow("imahe", cam1)
    cv2.waitKey(0) 

    s1 = (101* 3.4343,265* 3.4343)
    e1 = (687* 3.4343,325* 3.4343)
    cam11 = cv2.rectangle(img,(int(101* 3.4343),int(265* 3.4343)) ,(int(687* 3.4343),int(325* 3.4343)), color=(0,255,0),thickness=2)
    cv2.imshow("imahe", cam11)
    cv2.waitKey(0) 

    normal = [687.0,101.0,265.0,325.0]
    rotated = [101.0,265.0,687.0,325.0]



def values_check():
    xmin = 350
    ymin = 1828 
    xmax = 4000
    ymax = 1823

    max_width = 3000
    max_height = 1536

    if xmin<=0 : xmin = 0
    elif xmin <= max_width: xmin = xmin
    else: xmin = max_width

    if xmax<=0 : xmax = 0
    elif xmax <= max_width: xmax = xmax
    else: xmax = max_width

    if ymin<=0 : ymin = 0
    elif ymin <= max_height: ymin = ymin
    else: ymin = max_height

    if ymax<=0 : ymax = 0
    elif ymax <= max_height: ymax = ymax
    else: ymax = max_height
    print(xmin,ymin,xmax,ymax)



def r_w_csv():
    df = pd.read_csv("E:/Coding/Python/matrix_training/task-1/data/new_pavement_distress.csv")
    polygon_imgs =df['ImageName'].where(df['BoundingBoxType'] == 'Polygon')
    rectangle_imgs =df['ImageName'].where(df['BoundingBoxType'] == 'Polygon')

x =[]
y = []
def calculator():
    x1 =10
    y1 =438
    x2 =1591
    y2 =163
    # data = [(1528.0, 39.0), (1557.0, 39.0), (1563.0, 65.0), (1527.0, 72.0)]
    # data = [(100.0, 63.0), (104.0, 70.0), (431.0, 193.0), (841.0, 194.0), (911.0, 309.0), (1133.0, 432.0), (1783.0, 444.0), (1784.0, 419.0), (1225.0, 416.0), (822.0, 147.0), (419.0, 152.0)]
    # data = [10.0, 438.0, 1591.0, 163.0]
    # print(data[0][0])
    # for i in data:
    #     print(i)
    #     x.append(int(i[0]*3.4343))
    #     y.append(int(i[1]*3.4722))
    # print(x)
    # print(y)
    # print("xmin = ",min(x))
    # print("xmax = ",(max(x)))
    # print("ymin = ",min(y))
    # print("ymax = ",(max(y)))

    x1 = int(x1* 3.4343)  ####|
    y1 = int(y1* 3.4722)  ####|
    x2 = int(x2* 3.4343)  ####|>>Multiplying to match the original co-ordinates
    y2 = int(y2* 3.4722)

    print(x1,y1,x2,y2)
calculator()

def min_max_check():
    x1 =31 
    y1 = 5
    x2 = 7
    y2 = 1
    if x1>x2: x1,x2 = x2,x1
    print(x1,x2)
# min_max_check()

def plot_polygon():
    image = cv2.imread("E:\\Coding\\Python\\matrix_training\\task-1\\data\\images\\2022_06_01_11_17_46_160927_Distress.jpg")
    
        # Python program to explain
    # cv2.polylines() method



    # path
    # path = image

    # # Reading an image in default
    # # mode
    # image = cv2.imread(path)

    # Window name in which image is
    # displayed
    window_name = 'Image'

    # Polygon corner points coordinates
    pts = np.array([[3200,3236], [3214, 3249],
                    [3502, 3541], [4337, 4385],
                    [5278,5336], [6099, 6166], [6102,6170], [5800, 5864], [4835, 4888], [4018, 4062], [3551, 3590]],np.int32)

    # pts = pts.reshape((-1, 1, 2))

    isClosed = True

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 50

    # Using cv2.polylines() method
    # Draw a Blue polygon with
    # thickness of 1 px
    image = cv2.polylines(image, [pts],
                        isClosed, color, thickness)

    # Displaying the image
    cv2.imwrite("E:\\Coding\\Python\\matrix_training\\task-1\\data\\images\\2022_06_01_11_17_46_160927_Distress_polygon.jpg",image)
    while(1):
        
        cv2.imshow('image', image)
        if cv2.waitKey(20) & 0xFF == 27:
            break
            
    cv2.destroyAllWindows()
# plot_polygon()
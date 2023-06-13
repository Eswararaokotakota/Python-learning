import cv2
import os
import pandas as pd
import ast


df = pd.read_csv("E:/Coding/Python/matrix_training/task-1/data/new_pavement_distress.csv")
images_path = "E:\\Coding\\Python\\matrix_training\\task-1\\data\\images\\"
img_list = os.listdir(images_path)
polygon_lst = [] #list with nan values
polygon_lst1 = [] #list without nan values (polygon image names)
polygon_x_points= []
polygon_y_points= []

polygon_imgs =df['ImageName'].where(df['BoundingBoxType'] == 'Polygon')
# print(polygon_imgs)
polygon_lst.append(polygon_imgs.tolist())
for element in polygon_lst[0]:
    if str(element) != "nan":
        polygon_lst1.append(element)
# print(polygon_lst1[0])
count = 0
for i in polygon_lst1:
    imginfo = df[df['ImageName'] == i]
    imginfo = pd.DataFrame(imginfo)
    BoundingBox = imginfo["BoundingBox"]
    BoundingBox.tolist()
    BoundingBox = sorted(BoundingBox)
    # print(BoundingBox)
    polygon_points = ast.literal_eval(BoundingBox[0])
    # print(len(polygon_points),polygon_points,type(polygon_points))
    # print(polygon_points[0])
    count_1 = 0
    for j in polygon_points:
        # print(polygon_points[count_1])
        points_x = polygon_points[count_1][0]
        points_y = polygon_points[count_1][1]
        polygon_x_points.append(points_x)
        polygon_y_points.append(points_y)
        x1 = min(polygon_x_points)
        x2 = max(polygon_x_points)
        y1 = min(polygon_y_points)
        y2 = max(polygon_y_points)
        count_1+=1
        # print(count_1)
    print(x1,y1,x2,y2)
    polygon_x_points.clear()
    polygon_y_points.clear()

    count+=1
    if count == 1:
        break

import cv2
import os
import pandas as pd
import ast
import csv

df = pd.read_csv("E:/Coding/Python/matrix_training/task-1/data/pavement_distress.csv") #csv file path to read
images_path = "E:\\Coding\\Python\\matrix_training\\task-1\\data\\sharedata\\" #images path
folder_path = "E:\\Coding\\Python\\matrix_training\\task-1\\data\\rotated_images\\" #Resultant images are saved in this path

#------Creates a folder to save resultant images------- 
isExist = os.path.exists(folder_path)
if not isExist:
   os.makedirs(folder_path)

# os.listdir(images_path)
# print(img_list)

image_name = []
image_classes = []
BoundingBoxType_lst = []

polygon_lst = []
polygon_lst1 = []
polygon_x_points=[]
polygon_y_points=[]

cameras =[]
# cam1_lst = []
# cam2_lst = []
# cam3_lst = []
# cam4_lst = []
cam_names = []

x1_y1_x2_y2 = []

csv_file_writer = open("E:/Coding/Python/matrix_training/task-1/data/manipulated.csv","w",newline="")
Headers = ["ImageName","Xmin,Ymin,Xmax,Ymax","DestressClass","BoundingBoxType"]
writer = csv.writer(csv_file_writer)
writer.writerow(Headers)


def cam_crop():
    # print(len(polygon_lst1))
    if (main_image_name.endswith(".jpg")): 
        image_name.append(main_image_name)
        image = cv2.imread (os.path.join(images_path,main_image_name))
        size = image.shape
        crop_size = int(size[1]/4)
        cam1 = cv2.rotate(image[:, 0:crop_size], cv2.ROTATE_90_COUNTERCLOCKWISE)
        cam2 = cv2.rotate(image[:,crop_size:crop_size*2], cv2.ROTATE_90_COUNTERCLOCKWISE)
        cam3 = cv2.rotate(image[:,crop_size*2:crop_size*3], cv2.ROTATE_90_COUNTERCLOCKWISE)
        cam4 = cv2.rotate(image[:,crop_size*3:crop_size*4], cv2.ROTATE_90_COUNTERCLOCKWISE)
        i = main_image_name.replace('.jpg',"_")
        # print("cropped image",i)
        cv2.imwrite(folder_path+i+"cam1.jpg",cam1)
        cv2.imwrite(folder_path+i+"cam2.jpg",cam2)
        cv2.imwrite(folder_path+i+"cam3.jpg",cam3)
        cv2.imwrite(folder_path+i+"cam4.jpg",cam4)
        cameras.extend([cam1,cam2,cam3,cam4])

        cam1_name = i+"cam1.jpg"
        cam2_name = i+"cam2.jpg"
        cam3_name = i+"cam3.jpg"
        cam4_name = i+"cam4.jpg"
        cam_names.extend([cam1_name,cam2_name,cam3_name,cam4_name])

 
def polygon_points():  #------Converts the polygon points to the rectangle points--------
    polygon_points = ast.literal_eval(image_info[k])
    # polygon_points.tolist()
    count_1 = 0
    for j in polygon_points:
        points_x = j[0]
        points_y = j[1]
        polygon_x_points.append(points_x)
        polygon_y_points.append(points_y)
        x1poly = int(min(polygon_x_points))
        x2poly = int(max(polygon_x_points))
        y1poly = int(min(polygon_y_points))
        y2poly = int(max(polygon_y_points))
        count_1+=1
    x1_y1_x2_y2.clear()
    x1_y1_x2_y2.extend([x1poly,y1poly,x2poly,y2poly])
    polygon_x_points.clear()
    polygon_y_points.clear()
   

count_main = 0
for i in os.listdir(images_path):
    # print(i)
    main_image_name = i
    cameras =[]
    cam_crop()
    imginfo = df[df['ImageName'] == i]
    imginfo = pd.DataFrame(imginfo)
    BoundingBox = imginfo["BoundingBox"]
    # print(BoundingBox)
    BoundingBox.tolist()
    BoundingBox = sorted(BoundingBox)
    image_classes.append(BoundingBox)
    # print("image_classes",image_classes)
    BoundingBoxType = imginfo["BoundingBoxType"]
    BoundingBoxType.tolist()
    BoundingBoxType = sorted(BoundingBoxType)
    BoundingBoxType_lst.append(BoundingBoxType)

    Distress_Class = imginfo["Distress_Class"]
    Distress_Class.tolist()
    Distress_Class = sorted(Distress_Class)

    count_images = 0
    

    for image_info in image_classes: #-------------Will iterate through the BoundingBox co-ordinates and re_assign co-ordinates values as per the rotation---------- 
        duplicates = range(len(image_info))
        # print(duplicates)
        # print(ast.literal_eval(image_info[0])[0],ast.literal_eval(image_info[0])[1],ast.literal_eval(image_info[0])[2],ast.literal_eval(image_info[0])[3])
        for k in duplicates:
            # print(k)
            # print("image info",image_info[k])
            Distress_Class_name = Distress_Class[k]
            BoundingBoxType_name = BoundingBoxType[k]
            # print(BoundingBoxType_lst[0][k])
            if "Polygon" == BoundingBoxType_lst[0][k]: #If the points are polygon points then calls the polygon_points method
                polygon_points()

            elif "Rectangle" == BoundingBoxType_lst[0][k]: #Getting rectangle points
                # print("Its a rectangle")
                x1rect = int(ast.literal_eval(image_info[k])[0] )  ####|
                y1rect= int(ast.literal_eval(image_info[k])[1] )  ####|
                x2rect = int(ast.literal_eval(image_info[k])[2] )  ####|>>Multiplying to match the original co-ordinates
                y2rect = int(ast.literal_eval(image_info[k])[3] )  ####|

                #checking the min and max values to assign xmin and xmax
                if x1rect > x2rect: 
                    x1rect,x2rect = x2rect,x1rect
                if y1rect > y2rect:
                    y1rect,y2rect = y2rect,y1rect

                x1_y1_x2_y2.clear()
                x1_y1_x2_y2.extend([x1rect,y1rect,x2rect,y2rect])
                # print(x1_y1_x2_y2)

            #Applying the values after rotation
            x1 = x1_y1_x2_y2[0]
            y1 = x1_y1_x2_y2[1]
            x2 = x1_y1_x2_y2[2]
            y2 = x1_y1_x2_y2[3]

            x1 = int(x1* 3.4343)  ####|
            y1 = int(y1* 3.4722)  ####|
            x2 = int(x2* 3.4343)  ####|>>Multiplying to match the original co-ordinates
            y2 = int(y2* 3.4722)  ####|
            #Applying the values after rotation

            # x1 = 1600
            # x2 = 6000
            # y1 = 218
            # y2 = 1510

            xmin = y1
            ymin = 1536-x2
            xmax = y2
            ymax = 1536-x1
            # print(xmin,ymin,xmax,ymax) 

            cam_count = 0
#---------------This loops will gives the resultant co-ordinates for each cropped photo------------------
            for cam in cameras:
                # print(cam.shape)
                # print (cam_count)
                # max_width = cam1.shape[1] #3000         #width of the image
                max_height = 1536 #cam1.shape[0] 
                if cam_count == 0:

                    a = 0
                    b = 3000
                    c=0
                    d=1536

                    if xmin<=a : xmin1 = a
                    elif xmin <= b and xmin>a: xmin1 = xmin
                    else: xmin1 = b

                    if xmax<=a : xmax1 = a
                    elif xmax <= b and xmax>a: xmax1 = xmax
                    else: xmax1 = b

                    if ymin<=0 : ymin1 =0
                    elif ymin <= max_height and ymin>0: ymin1 = ymin
                    else: ymin1 = max_height

                    if ymax<=0 : ymax1 = 0
                    elif ymax <= d and ymax>c: ymax1 = ymax
                    else: ymax1 = max_height

                    # cam1_lst.append([xmin1,ymin1,xmax1,ymax1])
                    xy_points = xmin1,ymin1,xmax1,ymax1
                    # print(ymin1,ymax1)
                    if ymin1<=0 and ymax<=0:   
                        pass
                    else: 
                        writer.writerow([cam_names[cam_count],xy_points,Distress_Class_name,BoundingBoxType_name])

                elif cam_count == 1:
                    a = 0
                    b = 3000
                    c=1536
                    d=3072

                    if xmin<=a : xmin2 = a
                    elif xmin <= b and xmin>a: xmin2 = xmin
                    else: xmin2 = b

                    if xmax<=a : xmax2 = a
                    elif xmax <= b and xmax>a: xmax2 = xmax
                    else: xmax2 = b
                    

                    if ymin<=0 : 
                        ymin2 = max_height+ymin
                        if ymin2 <=0 : 
                            ymin2 = 0
                    else: ymin2 = max_height

                    
                    if ymax<=0 : 
                        ymax2 = max_height+ymax
                        if ymax2 <=0 : 
                            ymax2 = 0
                    else: ymax2 = max_height
                    # cam2_lst.append([xmin2,ymin2,xmax2,ymax2])
                    xy_points = xmin2,ymin2,xmax2,ymax2
                    # print(ymin2,ymax2)
                    grater = ymin2 >= max_height and ymax2 >= max_height
                    lesser = ymin2 <= 0 and ymax2 <= 0
                    if grater or lesser:
                        pass
                    else:
                        writer.writerow([cam_names[cam_count],xy_points,Distress_Class_name,BoundingBoxType_name])

                elif cam_count == 2:
                    a = 0
                    b = 3000
                    c=3072
                    d=4608

                    if xmin<=a : xmin3 = a
                    elif xmin <= b and xmin>a: xmin3 = xmin
                    else: xmin3 = b

                    if xmax<=a : xmax3 = a
                    elif xmax <= b and xmax>a: xmax3 = xmax
                    else: xmax3 = b
                    
                    if ymin<=0 : 
                        ymin3 = max_height+ymin  #even lesser than two images
                        if ymin3 <=0:
                            ymin3 = max_height+ymin3
                            if ymin3 <=0: #even lessthan 3 images
                                ymin3 = 0
                        else: ymin3 = max_height
                    else: ymin3 = max_height
                    
                    
                    if ymax<=0 : 
                        ymax3 = max_height+ymax  #even lesser than two images
                        if ymax3 <=0:
                            ymax3 = max_height+ymax3
                            if ymax3 <=0: #even lessthan 3 images
                                ymax3 = 0
                        else: ymax3 = max_height
                    else:
                        ymax3 = max_height
                    # cam3_lst.append([xmin3,ymin3,xmax3,ymax3])
                    xy_points = xmin3,ymin3,xmax3,ymax3
                    # print(ymin3,ymax3)
                    grater = ymin3 >= max_height and ymax3 >= max_height
                    lesser = ymin3 <= 0 and ymax3 <= 0
                    if grater or lesser:
                        pass
                    else:
                        writer.writerow([cam_names[cam_count],xy_points,Distress_Class_name,BoundingBoxType_name])

                elif cam_count == 3:
                    a = 0
                    b = 3000
                    c=4608
                    d=6144

                    if xmin<=a : xmin4 = a
                    elif xmin <= b and xmin>a: xmin4 = xmin
                    else: xmin4 = b

                    if xmax<=a : xmax4 = a
                    elif xmax <= b and xmax>a: xmax4 = xmax
                    else: xmax4 = b
                    
                    # print(ymin)
                    if ymin<=0 : 
                        ymin4 = max_height+ymin  #even lesser than two images
                        if ymin4 <=0:
                            ymin4 = max_height+ymin4                         
                            if ymin4 <=0 : #even lessthan 3 images
                                ymin4 = max_height+ymin4   
                            else: ymin4 = max_height                              
                        else:ymin4 = max_height
                    else:
                        ymin4 = max_height   
                    
                    if ymax<=0 : 
                        ymax4 = max_height+ymax  #even lesser than two images
                        if ymax4 <=0:
                            ymax4 = max_height+ymax4
                            if ymax4 <=0: #even lessthan 3 images
                                ymax4 = max_height+ymax4
                            else: ymax4 = max_height
                        else: ymax4 = max_height
                    else:
                        ymax4 = max_height
                    
                    # cam4_lst.append([xmin4,ymin4,xmax4,ymax4])
                    xy_points = xmin4,ymin4,xmax4,ymax4
                    # print(ymin4,ymax4)
                    grater = ymin3 >= max_height and ymax3 >= max_height
                    lesser = ymin3 <= 0 and ymax3 <= 0
                    if grater or lesser:
                        pass
                    else:
                        writer.writerow([cam_names[cam_count],xy_points,Distress_Class_name,BoundingBoxType_name])
                
                
                
                cam_count +=1
        cam_names.clear()
        count_images+=1
        if count_images==1:
            break
    image_classes.clear()
    BoundingBoxType_lst.clear()
    

csv_file_writer.close()
print("Done....!")
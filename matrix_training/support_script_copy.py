import cv2
import os
import pandas as pd
import ast
import csv

df = pd.read_csv("E:/Coding/Python/matrix_training/task-1/data/pavement_distress.csv")
images_path = "E:\\Coding\\Python\\matrix_training\\task-1\\data\\images\\"
folder_path = "E:\\Coding\\Python\\matrix_training\\task-1\\data\\rotated_images\\"

isExist = os.path.exists(folder_path)
if not isExist:
   os.makedirs(folder_path)

img_list = os.listdir(images_path)
# print(img_list)

image_name = []
image_classes = []
BoundingBoxType_lst = []

polygon_lst = []
polygon_lst1 = []
polygon_x_points=[]
polygon_y_points=[]

cameras =[]
cam1_lst = []
cam2_lst = []
cam3_lst = []
cam4_lst = []
cam_names = []

x1_y1_x2_y2 = []
x1_point  = []
y1_point  = []
x2_point  = []
y2_point  = []
    
# polygon_imgs =df['ImageName'].where(df['BoundingBoxType'] == 'Polygon')
# polygon_lst.append(polygon_imgs.tolist())
# for element in polygon_lst[0]:
#         if str(element) != "nan":
#             polygon_lst1.append(element)

csv_file_writer = open("E:/Coding/Python/matrix_training/task-1/data/manipulated.csv","w",newline="")
Headers = ["ImageName","Xmin,Ymin,Xmax,Ymax","DestressClass","BoundingBoxType"]
writer = csv.writer(csv_file_writer)
writer.writerow(Headers)


def cam_crop():
    # print(len(polygon_lst1))
    if (main_image_name.endswith(".jpg")): 
        # print(main_image_name)
        # print(i)
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

 
def polygon_points():
    # imginfo = df[df['ImageName'] == i]
    # print("Hei polygon")
    # print(i)
    # print(k)
    # imginfo = pd.DataFrame(imginfo)
    # BoundingBox = imginfo["BoundingBox"]
    # BoundingBox.tolist()
    # BoundingBox = sorted(BoundingBox)
    # # print(BoundingBox)
    # polygon_points = ast.literal_eval(BoundingBox[k])
    
    polygon_points = ast.literal_eval(image_info[k])
    # polygon_points.tolist()
    # print("polygonPoints",polygon_points)
    # print("polygonPoints",polygon_points[0])
    # print("polygonPointsk",polygon_points[k])
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
    # print("x",polygon_x_points)
    # print("y",polygon_y_points)
    polygon_x_points.clear()
    polygon_y_points.clear()
    # print(x1_y1_x2_y2)
    # print("polygon", x1poly,y1poly,x2poly,y2poly)
   

count_main = 0
for i in img_list:
    print(i)
    main_image_name = i
    cam_crop()
    # for j in polygon_lst1 :
    #     if i == j:
    #         polygon_points()
    # print(i)
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
    # Distress_Class = (Distress_Class)
    # print(Distress_Class[0])

    # print(BoundingBoxType_lst)
    # BoundingBox =  ast.literal_eval(BoundingBox)
    
    # if "Polygon" == BoundingBoxType_lst[0][0]:
    #     print("Hei Polygon")
    #     polygon_points()

        # print(count)
        # print(len(img_list))
    # if count == 1:
    count_images = 0
    

    for image_info in image_classes: #-------------Will iterate through the BoundingBox co-ordinates and re_assign co-ordinates values as per the rotation---------- 
        # print(image_classes[0])
        duplicates = range(len(image_info))
        print(duplicates)
       
        # i= ast.literal_eval(image_info[0])
        # print(ast.literal_eval(image_info[0])[0],ast.literal_eval(image_info[0])[1],ast.literal_eval(image_info[0])[2],ast.literal_eval(image_info[0])[3])
        for k in duplicates:
            print(k)
            # print("image info",image_info[k])
            # print(len(BoundingBoxType_lst))
            # print(BoundingBoxType_lst[0][k])
            # print(Distress_Class)
            Distress_Class_name = Distress_Class[k]
            BoundingBoxType_name = BoundingBoxType[k]
            # print(BoundingBoxType_lst)
            # print(BoundingBoxType_lst[0][k])
            if "Polygon" == BoundingBoxType_lst[0][k]:
                polygon_points()

            elif "Rectangle" == BoundingBoxType_lst[0][k]: #Getting rectangle points
                # print("Its a rectangle")
                x1rect = int(ast.literal_eval(image_info[k])[0] )  ####|
                y1rect= int(ast.literal_eval(image_info[k])[1] )  ####|
                x2rect = int(ast.literal_eval(image_info[k])[2] )  ####|>>Multiplying to match the original co-ordinates
                y2rect = int(ast.literal_eval(image_info[k])[3] )  ####|
                
                print(x1rect,y1rect,x2rect,y2rect) 
                if x1rect > x2rect: 
                    x1rect,x2rect = x2rect,x1rect
                if y1rect > y2rect:
                    y1rect,y2rect = y2rect,y1rect
                print(x1rect,y1rect,x2rect,y2rect)    

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
            xmin = y1
            ymin = 1536-x2
            xmax = y2
            ymax = 1536-x1
            print(xmin,ymin,xmax,ymax) 
    # def cam_points_comparision():
            # print(cam_names)
            cam_count = 0
            for cam in cameras:#---------------This loops will gives the resultant co-ordinates for each cropped photo------------------
                # print(cam.shape)
                # print("Comparision started")
                # print (cam_count)
                # max_width = cam1.shape[1] #3000         #width of the image
                max_height = 1536 #cam1.shape[0] 
                # print("max_height",max_height)
                if cam_count == 0:
                    # print(cam_count)

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

                    if ymax<=c : ymax1 = c
                    elif ymax <= d and ymax>c: ymax1 = ymax
                    else: ymax1 = max_height

                    # if ymin1 == 0 and ymax1 == 0:
                    #     print("No bounding box points in the picture-1")
                    cam1_lst.append([xmin1,ymin1,xmax1,ymax1])
                    # print(cam1_lst)
                    xy_points = xmin1,ymin1,xmax1,ymax1
                    # cam_name = cam_names[cam_count]
                    writer.writerow([cam_names[cam_count],xy_points,Distress_Class_name,BoundingBoxType_name])

                elif cam_count == 1:
                    # print(cam_count)
                    # print(cam_names[cam_count])
                    # print(Distress_Class_name)
                    # print(BoundingBoxType_name)
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
                        # ymin2 = c
                    # elif ymin <= d and ymin>c:
                    #     ymin2 = max_height-ymin
                    #     ymin2 = ymin
                    else: ymin2 = max_height

                    
                    if ymax<=0 : 
                        ymax2 = max_height+ymax
                        if ymax2 <=0 : 
                            ymax2 = 0
                    # elif ymax <= d and ymax>c:
                    #     ymax2 = max_height-ymax
                        # yma
                        # x2 = ymax
                    else: ymax2 = max_height

                    
                    # if ymin2 == max_height and ymax == max_height:
                    #     print("No bounding box points in the picture-2")
                    cam2_lst.append([xmin2,ymin2,xmax2,ymax2])
                    # print(cam2_lst)
                    xy_points = xmin2,ymin2,xmax2,ymax2
                    # cam_name = cam_names[cam_count]
                    writer.writerow([cam_names[cam_count],xy_points,Distress_Class_name,BoundingBoxType_name])
                    # print(xmin2,ymin2,xmax2,ymax2)

                elif cam_count == 2:
                    # print(cam_count)
                    # print(cam_names[cam_count])
                    # print(Distress_Class_name)
                    # print(BoundingBoxType_name)
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
                        # print(ymin3)
                        if ymin3 <=0:
                            ymin3 = max_height+ymin3
                            if ymin3 <=0: #even lessthan 3 images
                                ymin3 = 0
                        else: ymin3 = max_height
                    else: ymin3 = max_height
                    # else: ymin3 = 0
                    # if ymin <= 0: ymin3 = 0
                    # elif ymin <= d and ymin>c: ymin3 = ymin
                    # else: ymin3 = d
                    
                    if ymax<=0 : 
                        ymax3 = max_height+ymax  #even lesser than two images
                        if ymax3 <=0:
                            ymax3 = max_height+ymax
                            if ymax3 <=0: #even lessthan 3 images
                                ymax3 = 0
                        else: ymax3 = max_height
                    else:
                        ymax3 = max_height
                    # if ymax<=c : ymax3 = c
                    # elif ymax <= d and ymax>c: ymax3 = ymax
                    # else: ymax3 = d
                    
                    # if ymin3 == max_height and ymax3 == max_height:
                    #     print("No bounding box points in the picture-3")
                    cam3_lst.append([xmin3,ymin3,xmax3,ymax3])
                    # print(cam3_lst)
                    xy_points = xmin3,ymin3,xmax3,ymax3
                    # cam_name = cam_names[cam_count]
                    writer.writerow([cam_names[cam_count],xy_points,Distress_Class_name,BoundingBoxType_name])
                    # print(xmin3,ymin3,xmax3,ymax3)  

                elif cam_count == 3:
                    # print(cam_count)
                    # print(cam_names[cam_count])
                    # print(Distress_Class_name)
                    # print(BoundingBoxType_name)
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
                    print(ymin)
                    if ymin<=0 : 
                        ymin4 = max_height+ymin  #even lesser than two images
                        print(ymin4)
                        if ymin4 <=0:
                            ymin4 = max_height+ymin4
                            print(ymin4)
                            if ymin4 <=0 : #even lessthan 3 images
                                ymin4 = max_height+ymin4
                                print(ymin4)
                        else:ymin4 = max_height
                        # else: ymin4 = max_height
                    else:
                        ymin4 = max_height
                    # if ymin<=c : ymin4 = c
                    # elif ymin <= d and ymin>c: ymin4 = ymin
                    # else: ymin4 = d
                    # print(ymax)
                    if ymax<=0 : 
                        ymax4 = max_height+ymax  #even lesser than two images
                        if ymax4 <=0:
                            ymax4 = max_height+ymax4
                            if ymax4 <=0: #even lessthan 3 images
                                ymax4 = max_height+ymax4
                            # else: ymax4 = max_height
                        else: ymax4 = max_height
                    else:
                        ymax4 = max_height
                    # else: ymax4 = max_height
                    # if ymax<=c : ymax4 = c
                    # elif ymax <= d and ymax>c: ymax4 = ymax
                    # else: ymax4= d
                    # if ymin4 == max_height and ymax4 == max_height:
                    #     print("No bounding box points in the picture-4")
                    cam4_lst.append([xmin4,ymin4,xmax4,ymax4])
                    # print(cam4_lst)
                    xy_points = xmin4,ymin4,xmax4,ymax4
                    # cam_name = cam_names[cam_count]
                    writer.writerow([cam_names[cam_count],xy_points,Distress_Class_name,BoundingBoxType_name])
                    # print(xmin4,ymin4,xmax4,ymax4,"\n")

                # cam1_lst.extend([xmin,ymin,xmax,ymax])
                cam_count +=1
        cam_names.clear()
                # print(count)
                # print(xmin,ymin,xmax,ymax)
        # print("cam_names",cam_names)
        count_images+=1
        if count_images==1:
            break
    # count_main+=1
    image_classes.clear()
    BoundingBoxType_lst.clear()
    # if count_main ==1:
    #     break
csv_file_writer.close()
        # print(xmin,ymin,xmax,ymax)
            
        # print(crop_size)
        # print(len(cameras))

        # plot1 = cv2.rectangle(cam1, x1)   
            
















    # csvdata = pd.read_csv("E:/Coding/Python/matrix_training/task-1/data/pavement_distress.csv")
    # csvdata.to_csv("E:/Coding/Python/matrix_training/task-1/data/new_pavement_distress.csv")
    # input_csv = pd.DataFrame(csvdata)
    # # print(image_name[1])
    # get_row = input_csv[input_csv['ImageName'] == image_name[0]].index
    # # print(get_row)

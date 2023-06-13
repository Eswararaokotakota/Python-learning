import cv2
import csv
import os
import ast
d={}
All_rows=[]
file_path=r"E:\Coding\Python\PROJECTS\ML\review_modify_labled_data\Distress_Check_with_File_Path.csv"
i=1
if os.path.exists(file_path):
    with open(file_path,'r')as file:
       Id=csv.reader(file)
       Id=list(Id)
       print(len(Id))
       print(Id)
       if len(Id)>1:
           print(i)
           print(Id[-1][-1])
           i=int(Id[-1][-1])
           
if len(All_rows)>0:
    if not os.path.exists(file_path+"_checked.csv"):
        All_rows.insert(0,["ImageName","Xmin,Ymin,Xmax,Ymax","DistressClass","BoundingBoxType","ID"])
           
with open(file_path+'.csv','r')as file:
   filecontent=csv.reader(file)
   cnt=0
   filecontent=list(filecontent)
   length=len(filecontent)
   print(length)
##   for row in filecontent:
   
   
   while(True):
    if cnt!=0:
        row=filecontent[i].copy()
        row.append(i)
        bbox=ast.literal_eval(row[1])
        cls=row[2]
        if cls in d:
            d[cls]=d[cls]+1
        else:
            d[cls]=1
        print(row[0])
        img=cv2.imread(os.path.join("RotatedImages",row[0]))
          
        font = cv2.FONT_HERSHEY_SIMPLEX
        image = cv2.rectangle(img, (bbox[0],bbox[1]), (bbox[2],bbox[3]), [255,0,0],2)
        image=cv2.putText(image,cls, (int((bbox[0]+bbox[2])/2),int((bbox[1]+bbox[3])/2)),font, 0.9, (36,255,12), 2)
##        image=cv2.putText(image,cls, (bbox[0],bbox[1]),font, 0.9, (36,255,12), 2)
        cv2.imshow("Image",cv2.resize(image,(1789,865)))
        key=cv2.waitKey(0)
        if key==ord("q"):
            break
        elif key==ord("s"):
            if row not in All_rows:
                All_rows.append(row)
            with open(file_path+"_checked.csv",'a') as wf:
                writer=csv.writer(wf)
                writer.writerow(row)
            i+=1
            i=min(i,length-1)
##        elif key==ord("d"):
##            if row in All_rows:
##                All_rows.remove(row)
##            i+=1
##            i=min(i,length-1)
        elif key==ord("b"):
            i-=1
            i=max(1,i)
        else:
            i+=1
            i=min(i,length-1)
    cnt+=1
##    i+=1
cv2.destroyAllWindows()

        
    
print("Classes Information")
less_than_500_images=[]
total_classes=[]
for key in d:
    if d[key]<500:
        less_than_500_images.append(key)
    else:
        total_classes.append(key)
    print(key,":",d[key])
print(total_classes,len(total_classes))
print(less_than_500_images,len(less_than_500_images))

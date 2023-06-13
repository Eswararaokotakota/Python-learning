import cv2
import csv
import os

folder_path = "E:\\Coding\\Python\\openCV\\find_pixel_value\\images"
# image_path = "E:\\Coding\\Python\\openCV\\camera.jpg"
list = []
       

def on_mouse_click(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,"",y)
        first = x #width
        second = y  #height
        co_ordinates = [first,second]
        list.append(co_ordinates)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, str(x)+","+str(y),(x,y),font,0.5,(255,255,0),1)
        cv2.imshow("image", image) 

def save_to_text_file():
    path = "E:\\Coding\\Python\\openCV\\find_pixel_value\\"
    txt_file = open(path+"co_ordinates.txt","a")
    txt_file.write("\n"+grid_name+"\n"+str(list))
    txt_file.close()  
          
def save_to_csv():
    file =open("E:\\Coding\\Python\\openCV\\find_pixel_value\\co_ordinates.csv","a")
    writer = csv.writer(file)
    writer.writerow(list)
    file.close()


############################ Reading Image from folder ##########################
img_list = os.listdir(folder_path)

for filename in img_list:
    print(filename)
    #reading image
    image = cv2.imread (os.path.join(folder_path,filename))
    grid_name = input("Enter grid name(ex: grid point0)")

    # if __name__=="__main__": 
    print("Executing")
        # image = cv2.imread(img,1)
    print(image.shape)
    cv2.imshow("image",image)
    cv2.setMouseCallback('image', on_mouse_click)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(list)
    save_to_text_file()
    save_to_csv()
    list.clear()
print("Done!")





import cv2
import os
import numpy as np

# image_left = "E:\\Coding\\Python\\openCV\\warp_stitch\\l.jpg"
# image_right = "E:\\Coding\\Python\\openCV\\warp_stitch\\r.jpg"
path = "E:\\Coding\\Python\\openCV\\warp_stitch\\images"

list =[]
left_image = []
right_image = []

def on_mouse_click(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,"",y)
        first = x*4 #width
        second = y*4 #height
        co_ordinates = [first,second]
        list.append(co_ordinates)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(resized_image, str(x)+","+str(y),(x,y),font,0.5,(255,255,0),1)
        cv2.imshow("image", resized_image) 

def save_to_text_file():
    path = "E:\\Coding\\Python\\openCV\\warp_stitch\\"
    txt_file = open(path+"co_ordinates.txt","a")
    txt_file.write("left_image"+"\n"+str(list))
    txt_file.close()

############################ Reading Image from folder ##########################
image_list = os.listdir(path)

for filename in image_list:
    print(filename)
    #reading image
    image = cv2.imread (os.path.join(path,filename))
    # grid_name = input("Enter grid name(ex: grid point0)")
    resized_image =cv2.resize(image,(512,385))
    if __name__=="__main__": 
        print("Executing......")
        print(image.shape)
        print(resized_image.shape)
        cv2.imshow("image",resized_image)
        cv2.setMouseCallback('image', on_mouse_click)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(list)
        #####################--image warp--###########################
        width,height = 2048,1540
        points_l= np.float32(list) 
        tell_pos = np.float32([[0,0],[width,0],[0,height],[width,height]]) 
        matrix = cv2.getPerspectiveTransform(points_l,tell_pos)
        img_wrp =cv2.warpPerspective(image,matrix,(width,height))
        left_image.append(img_wrp)
        save_to_text_file()
        list.clear()
print("Done!")
left = left_image[0]
right = left_image[1]
stack = np.hstack((left,right))
# cv2.imshow("stacked", stack)
# cv2.waitKey(0)
cv2.imwrite("E:\\Coding\\Python\\openCV\\warp_stitch\\images\\stitched_img.jpg", stack)
print(stack.shape)
print("Done...!")

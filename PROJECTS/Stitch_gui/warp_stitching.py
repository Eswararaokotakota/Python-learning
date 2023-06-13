
import cv2
import os
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from browser import Ui_MainWindow
import sys

# image_left = "E:\\Coding\\Python\\openCV\\warp_stitch\\l.jpg"
# image_right = "E:\\Coding\\Python\\openCV\\warp_stitch\\r.jpg"


list =[]
left_image = []
right_image = []

class warp_stitch(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(warp_stitch,self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Browse.clicked.connect( self.run_stitch_code)
        
        # self.pathh = Ui_MainWindow()
        # self.path = self.pathh.Browse_folder()
        

    def on_mouse_click(self,event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(x,"",y)
            first = x*2 #width
            second = y*2 #height
            co_ordinates = [first,second]
            list.append(co_ordinates)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(self.resized_image, str(x)+","+str(y),(x,y),font,0.5,(255,255,0),1)
            cv2.imshow("image", self.resized_image) 

    def save_to_text_file(self):
        path_txt = "E:\\Coding\\Python\\openCV\\warp_stitch\\"
        txt_file = open(path_txt+"co_ordinates.txt","w")
        txt_file.write("left_image"+"\n"+str(list))
        txt_file.close()
  
    ############################ Reading Image from folder ##########################
    def run_stitch_code(self):
        self.close()
        self.file = QFileDialog.getExistingDirectory()
        self.path = self.file
        # path = "E:\\Coding\\Python\\openCV\\warp_stitch\\images"
        print("Is it the path?: ", self.path)
        try:
            image_list = os.listdir(self.path)

            for filename in image_list:
                print(filename)
                #reading image
                image = cv2.imread (os.path.join(self.path,filename))
                # grid_name = input("Enter grid name(ex: grid point0)")
                self.resized_image =cv2.resize(image,(1024,770))
                # if __name__=="__main__": 
                print("Executing......")
                print(image.shape)
                print(self.resized_image.shape)
                cv2.imshow("image",self.resized_image)
                cv2.setMouseCallback('image', self.on_mouse_click)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                print(list)
                #####################--image warp--###########################
                width,height = 2048,1540
                points_l= np.float32(list) 
                tell_pos = np.float32([[0,0],[width,0],[0,height],[width,height]]) 
                matrix = cv2.getPerspectiveTransform(points_l,tell_pos)
                img_wrp =cv2.warpPerspective(self.resized_image,matrix,(width,height))
                left_image.append(img_wrp)
                self.save_to_text_file()
                list.clear()
            left = left_image[0]
            right = left_image[1]
            stack = np.hstack((left,right))
            # cv2.imshow("stacked", stack)
                            # cv2.waitKey(0)
            cv2.imwrite("E:\\Coding\\Python\\openCV\\warp_stitch\\images\\stitched_img.jpg", stack)
            print(stack.shape,"stack shape")
            print("Done...!")

        except:
            print("Error.........!","\n","Once recheck tha path again")
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
   
    code = warp_stitch()
    code.show()
    
    sys.exit(app.exec_())
 
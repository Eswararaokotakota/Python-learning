import cv2
import numpy as np
import matplotlib.pyplot as plt
from random import randrange
img_ = cv2.imread('E:\Coding\Python\right_distress.png')
img1 = cv2.cvtColor(img_,cv2.COLOR_BGR2GRAY)
img = cv2.imread('left_distress.png')
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
# Apply ratio test
good = []
for m in matches:
	if m[0].distance < 0.5*m[1].distance:
		good.append(m)
		matches = np.asarray(good)
if len(matches[:,0]) >= 4:
	src = np.float32([ kp1[m.queryIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
	dst = np.float32([ kp2[m.trainIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
	H, masked = cv2.findHomography(src,dst, cv2.RANSAC, 5.0)
	print(H)
else:
	raise AssertionError('Can’t find enough keypoints.')
# t=np.array([[0,2048,2048,0],[0,0,1536,1536],[1,1,1,1]])
# H=H*t
#H=np.array([[7.23771893e-01,-3.00069838e-02,1.66032257e+03],[-4.12188833e-02,9.61271299e-01,-6.10075789e+01],[-1.42934852e-04,-2.16814493e-05,1.00000000e+00]])
#H1=np.array([[ 9.60806626e-01,-9.21532361e-02,1.18228877e+03],[5.79236355e-03,9.73743182e-01,-2.42186761e+01][-2.30567658e-05,-3.72204220e-05,1.00000000e+00]])
#img_ = cv2.imread('26_Asset3.png')
#img = cv2.imread('26_Asset2.png')
dst = cv2.warpPerspective(img_,H,(img.shape[1] + img_.shape[1], img.shape[0]))


plt.subplot(122),plt.imshow(dst),plt.title('Warped Image')
plt.show()
plt.figure()

dst[0:img.shape[0], 0:img.shape[1]] = img
cv2.imwrite('stritched_img.png',dst)
plt.imshow(dst)
plt.show()
###centre and right
#H=[[7.23771893e-01,-3.00069838e-02,1.66032257e+03],[-4.12188833e-02,9.61271299e-01,-6.10075789e+01],[-1.42934852e-04,-2.16814493e-05,1.00000000e+00]]
###left and centre
#H1=[[ 9.60806626e-01,-9.21532361e-02,1.18228877e+03],[5.79236355e-03,9.73743182e-01,-2.42186761e+01][-2.30567658e-05,-3.72204220e-05,1.00000000e+00]]
#vehicle centre and right
# [[ 7.74779058e-01,-4.40780779e-02,9.64421706e+02],[-7.99389302e-04,8.62040254e-01,7.31600242e+01],[-4.28801014e-05,-5.35642294e-05,1.00000000e+00]]
#vehicle left and centre
#[[ 9.30886889e-01,-2.15382581e-01,1.33163204e+03],[ 7.52653179e-02,8.59548676e-01,-3.77874992e+01],[-7.74990986e-06,-8.34562671e-05,1.00000000e+00]]

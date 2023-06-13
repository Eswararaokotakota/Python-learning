import cv2

cv2.IMREAD_COLOR #: Loads image in color. It is used by default.
cv2.IMREAD_GRAYSCALE #: Loads image in gray mode.
cv2.IMREAD_UNCHANGED #: Loads image as it is, including alpha channels.
opencv_version=cv2.__version__
print(opencv_version)
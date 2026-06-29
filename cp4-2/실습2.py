import numpy as np
import cv2

white = (255,255,255)

image = cv2.imread('lenna.bmp',cv2.IMREAD_COLOR_BGR)
pt1 = image.shape[0]//4
pt2 = image.shape[1]//4

for i in range(1,4):
    cv2.line(image,((pt1*i),image.shape[0]),((pt1*i),0),white,1)
    cv2.line(image,(image.shape[0],(pt1*i)),(0,(pt1*i)),white,1)

cv2.imshow('Lenna & Line',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

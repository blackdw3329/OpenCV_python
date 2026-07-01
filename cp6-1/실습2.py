import numpy as np
import cv2

image = cv2.imread('lenna.bmp',cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("파일 읽기 오류")

def on_change(value):
    bright = cv2.add(image,value)
    cv2.imshow("lenna bright",bright)


cv2.imshow("lenna bright",image)

cv2.createTrackbar("bright","lenna bright",0,100,on_change)

cv2.waitKey(0)
cv2.destroyAllWindows()

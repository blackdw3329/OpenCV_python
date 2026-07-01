import numpy as np
import cv2

image = cv2.imread('lenna.bmp',cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("파일 읽기 오류")

is_add = True

def on_mouse(event, x, y, flags, param):
    global image,is_add
    if event == cv2.EVENT_LBUTTONDOWN:
        if is_add == True:
            bright = cv2.add(image,10)
            image = bright
            cv2.imshow("lenna bright",image)
        elif is_add == False:
            dark = cv2.subtract(image,10)
            image = dark
            cv2.imshow("lenna bright",image)


def on_change(value):
    global is_add
    if value == 0:
        is_add = True
    elif value == 1:
        is_add = False


cv2.imshow("lenna bright",image)

cv2.createTrackbar("mode","lenna bright",0,1,on_change)
cv2.setMouseCallback("lenna bright",on_mouse)

cv2.waitKey(0)
cv2.destroyAllWindows()

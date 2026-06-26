import numpy as np
import cv2

Move_Total = 0
LDown_Total = 0
LUp_Total = 0

def onMouse(event, x, y, flags, param):

    global Move_Total
    global LDown_Total
    global LUp_Total

    if event == cv2.EVENT_LBUTTONDOWN:
        LDown_Total += 1
        print(f"EVENT_LBUTTONDOWN : {LDown_Total}")
    elif event == cv2.EVENT_LBUTTONUP:
        LUp_Total += 1
        print(f"EVENT_LBUTTONUP : {LUp_Total}")
    elif event == cv2.EVENT_MOUSEMOVE:
        Move_Total +=1
        print(f"EVENT_MOUSEMOVE : {Move_Total}")

image = cv2.imread('lenna.bmp',cv2.IMREAD_COLOR)
cv2.imshow('Mouse Event', image)
cv2.setMouseCallback('Mouse Event', onMouse)
while True:
    if cv2.waitKey(1000) == 27: break
cv2.destroyAllWindows()

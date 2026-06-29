import numpy as np
import cv2

image = np.zeros((500,500,3),np.uint8)
image.fill(255)

cv2.imshow('hi',image)

isMD = False
prevCursor = (0,0)
lineColor = (255,0,0)

def onMouse(event, x, y, flags, param):
    global isMD, prevCursor, image, lineColor
    if event == cv2.EVENT_LBUTTONDOWN:
        isMD = True
        prevCursor = (x,y)
    elif event == cv2.EVENT_LBUTTONUP:
        isMD = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if isMD:
            cv2.line(image,prevCursor,(x,y),lineColor,1)
            prevCursor = (x,y)
            cv2.imshow('hi',image)

def onChange(value):
    global lineColor
    if value == 0:
        lineColor = (255,0,0)
    elif value == 1:
        lineColor = (0,255,0)
    elif value == 2:
        lineColor = (0,0,255)



cv2.createTrackbar('color','hi',0,2,onChange)
cv2.setMouseCallback('hi',onMouse)

while True:
    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()

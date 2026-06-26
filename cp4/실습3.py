import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"좌표: ({x},{y}), 화소값(B, G, R): {int(image[x, y, 0]), int(image[x, y, 0]), int(image[x, y, 0])})")

image = cv2.imread('lenna.bmp',cv2.IMREAD_COLOR_BGR)
cv2.imshow('Mouse Event', image)
cv2.setMouseCallback('Mouse Event', onMouse)
while True:
    if cv2.waitKey(1000) == 27: break
cv2.destroyAllWindows()

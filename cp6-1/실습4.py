import numpy as np
import cv2

image = cv2.imread('lenna.bmp',cv2.IMREAD_GRAYSCALE)
po1 = (0,0)
po2 = (0,0)


def on_mouse(event,x,y,f,p):
    global pos1, pos2, image
    copy_img = image.copy()
    if event == cv2.EVENT_LBUTTONDOWN:
        pos1= (x,y)
        print(f"{pos1}")
    if event == cv2.EVENT_LBUTTONUP:
        pos2 = (x,y)
        max_pos = (max(pos1[0], pos2[0]),max(pos1[1],pos2[1]))
        min_pos = (min(pos1[0], pos2[0]),min(pos1[1],pos2[1]))
        copy_img[min_pos[1]:max_pos[1], min_pos[0]:max_pos[0]] = cv2.add(copy_img[min_pos[1]:max_pos[1], min_pos[0]:max_pos[0]],100)
        cv2.imshow("lenna bright",copy_img)
        print(f"{pos2}")


cv2.imshow("lenna bright",image)
cv2.setMouseCallback("lenna bright",on_mouse)

cv2.waitKey(0)
cv2.destroyAllWindows()

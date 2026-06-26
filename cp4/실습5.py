import numpy as np
import cv2



def onMouse(event, x, y, flags, param):
    global image

    if event == cv2.EVENT_LBUTTONDOWN:
        image[:,:,2].fill(255)
        image[:,:,1].fill(0)
        image[:,:,0].fill(0)
        cv2.imshow("Color change",image)
    elif event == cv2.EVENT_RBUTTONDOWN:
        image[:,:,2].fill(0)
        image[:,:,1].fill(0)
        image[:,:,0].fill(255)
        cv2.imshow("Color change",image)

image = np.zeros((200,400,3), np.uint8)
image.fill(255)
cv2.imshow("Color change", image)
cv2.setMouseCallback("Color change", onMouse)
while True:
    if cv2.waitKey(1000) == 27: break
cv2.destroyAllWindows()

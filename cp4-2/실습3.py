import numpy as np
import cv2

blue,green,red,white = (255,0,0), (0,255,0),(0,0,255),(255,255,255)

image = np.zeros((400,1200,3),np.uint8)
image.fill(0)
image_blue = image[:400,:400]
image_green = image[:400,400:800]
image_red = image[:400,800:1200]
image_blue[:] = blue
image_green[:] = green
image_red[:] = red

cv2.rectangle(image_blue,(100,100),(300,300),white,10)
cv2.circle(image_green,(image_green.shape[1]//2,image_green.shape[0]//2),100,white,10)
cv2.line(image_red,(100,100),(300,300),white,10)
cv2.line(image_red,(300,100),(100,300),white,10)

cv2.imshow('three color',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

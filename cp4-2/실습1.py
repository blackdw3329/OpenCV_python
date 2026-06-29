import numpy as np
import cv2

image = np.zeros((400, 400), np.uint8)
image2 = np.zeros((400, 400), np.uint8)
image.fill(255)
image2.fill(255)
pt1, pt2 = (300, 300), (100,100)
pt4, pt5 = (300, 100), (100,300)

# 사선두개 사각형
cv2.line(image, pt1, pt2,0,1)
cv2.line(image, pt4, pt5,0,1)
cv2.rectangle(image, pt1, pt2,0,1)
cv2.imshow('Line & Rectangle', image)

# 내접원 사각형
cv2.rectangle(image2, pt1, pt2,0,1)
cv2.circle(image2, (image2.shape[1]//2,image2.shape[0]//2), 100,0)
cv2.imshow('Circle & Rectangle', image2)

cv2.waitKey(0)
cv2.destroyAllWindows()

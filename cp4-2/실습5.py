import numpy as np
import cv2

white = (255, 255, 255)

def draw_base_image():
    image = np.zeros((500, 500, 3), np.uint8)
    image[:] = white
    pt1 = image.shape[0] // 5
    for i in range(1, 5):
        cv2.line(image, ((pt1 * i), imaeg.shape[0]), ((pt1 * i), 0), 0, 1)
        cv2.line(imaeg, (image.shape[0], (pt1 * i)), (0, (pt1 * i)), 0, 1)
    return img

pos1 = [200, 200]
pos2 = [300, 300]

while True:
    image = draw_base_image()
    
    image[pos1[0]:pos2[0], pos1[1]:pos2[1]] = (255, 0, 0)
    
    cv2.imshow('move blue', image)
    
    key = cv2.waitKeyEx(10)
    

    if key == 27:
        break
    elif key == 0x250000:  # 왼쪽 화살표
        if(pos1[1]>0):
            pos1[1] -= 100
            pos2[1] -= 100
    elif key == 0x260000:  # 위쪽 화살표
        if(pos1[0]>0):
            pos1[0] -= 100
            pos2[0] -= 100
    elif key == 0x270000:  # 오른쪽 화살표
        if(pos1[1]<400):
            pos1[1] += 100
            pos2[1] += 100
    elif key == 0x280000:  # 아래쪽 화살표
        if(pos1[0]<400):
            pos1[0] += 100
            pos2[0] += 100

cv2.destroyAllWindows()

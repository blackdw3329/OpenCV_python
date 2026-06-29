import numpy as np
import cv2

white = (255, 255, 255)
black = (0, 0, 0)

pos1 = [200, 200]
image = np.zeros((500, 500, 3), np.uint8)
image[:] = white
while True:
    
    pos2 = list(pos1)
    
    key = cv2.waitKeyEx(10)
    
    if key == ord('q'): 
        break
    elif key == 0x250000:  # 왼쪽 화살표
        pos2[0] -= 50
    elif key == 0x260000:  # 위쪽 화살표
        pos2[1] -= 50
    elif key == 0x270000:  # 오른쪽 화살표
        pos2[0] += 50
    elif key == 0x280000:  # 아래 화살표
        pos2[1] += 50
        
    pos2[0] = max(0, min(500, pos2[0]))
    pos2[1] = max(0, min(500, pos2[1]))
    
    cv2.line(image, tuple(pos1), tuple(pos2), black, 1)
    
    pos1 = pos2
    
    cv2.imshow('move line', image)

cv2.destroyAllWindows()

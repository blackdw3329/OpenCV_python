import numpy as np
import cv2

image = np.zeros((300, 300), np.uint8)
time_count = 0
is_running = False

while True:
    image.fill(255)
    
    time_str = str(round(time_count,1))
    
    cv2.putText(image, time_str, (80, 160), cv2.FONT_HERSHEY_DUPLEX, 2, 0)
    cv2.imshow('Stopwatch', image)
    
    key = cv2.waitKey(100)
    if is_running:
        time_count += 0.1
    if key == ord('s'):
        is_running = True
    elif key == ord('t'):
        is_running = False
    elif key == ord('r'):
        time_count = 0.0
    elif key == ord('q'):
        break
cv2.destroyAllWindows()

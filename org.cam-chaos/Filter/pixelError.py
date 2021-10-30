import cv2
import random
import time

import numpy as np

counter = 0
def pixelError(frames):
    global counter
    counter = counter +1
    points = ""
    for i in range(counter):
        points = points +"."
    if counter == 4:
        counter =0
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 2
    color = (0, 0, 0, 255)
    thickness = 3
    rows,cols,_ = frames.shape
    for i in range(rows):
        for j in range(cols):
            frames[i,j] = random.randint(0,255)
    frame= cv2.putText(frames, "Try to reconnect"+points, (20, 50), font, fontScale, color, thickness, cv2.FONT_HERSHEY_PLAIN)
            
        
    #print(np.array(picture1))

    return frames
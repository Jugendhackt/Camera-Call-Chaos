import numpy as np
import cv2
#from main import *
from Ascii import *

cap = cv2.VideoCapture(0)
i = True
while True:
    my_img_1 = np.zeros((1920, 1080, 1), dtype = "uint8")

    ret, frame = cap.read()
    org = (0, 50)
    

    
    lab= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame = cv2.cvtColor(lab, cv2.COLOR_BGR2GRAY)
    
    
    resized_img = cv2.resize(frame,(200,100))
    #ascii(resized_img)
    font = cv2.FONT_HERSHEY_SIMPLEX
    
  
# org
    org = (0, 40)
    
    # fontScale
    fontScale = 0.3
    
    color = (255, 0, 0)
    
    # Line thickness of 2 px
    thickness = 1
    frame = my_img_1
    
    # Using cv2.putText() method


    text = ascii(resized_img)
    y0, dy = 0, 10
    for i, line in enumerate(text.split('\n')):
        y = y0 + i*dy
        frame = cv2.putText(frame, line, (0, y ), font, 
                    fontScale, color, thickness, cv2.FONT_HERSHEY_PLAIN)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i = False

cap.release()
cv2.destroyAllWindows()
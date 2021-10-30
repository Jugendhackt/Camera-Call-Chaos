import cv2

import numpy as np

def binary(frames):


    lab= cv2.cvtColor(frames, cv2.COLOR_BGR2HSV)
    frame = cv2.cvtColor(lab, cv2.COLOR_BGR2GRAY)
    points = ""



    
    
    resized_img = cv2.resize(frame,(200,100))
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.3
    color = (0, 255, 0, 255)
    thickness = 1
    my_img_1 = np.zeros((1920, 1080, 3), dtype = "uint8")
    scale = 2/255
    gscale1 = "01"
    gscale = []
    frame = my_img_1
    for i3 in gscale1:
        gscale.append(i3)
    picture = ""
    
    for i in resized_img:
    
        
        for i2 in i*scale:
            try:
                picture = picture +gscale[int(i2+0.3)]
            except:
                picture = picture +gscale[1]


        picture = picture +" \n "

    y0, dy = 0, 10
    for i, line in enumerate(picture.split('\n')):
        y = y0 + i*dy
        frame= cv2.putText(frame, line, (0, y ), font, 
                    fontScale, color, thickness, cv2.FONT_HERSHEY_PLAIN)
    return frame

    


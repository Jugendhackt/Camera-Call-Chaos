import cv2

import numpy as np

def ascii(frames, width, height):

    lab= cv2.cvtColor(frames, cv2.COLOR_BGR2HSV)
    frame = cv2.cvtColor(lab, cv2.COLOR_BGR2GRAY)


    resized_img = cv2.resize(frame,(200,100))
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.3
    color = (0, 255, 0, 255)
    thickness = 1
    my_img_1 = np.zeros((height, width, 3), dtype = "uint8")
    scale = 9/255
    gscale1 = "@%#*+=-:. "
    gscale = []
    frame = my_img_1
    for i3 in gscale1:
        gscale.append(i3)
    picture = ""

    for i in resized_img:


        for i2 in i*scale:
            picture = picture +gscale[int(i2)]

        picture = picture +" \n "

    y0, dy = 0, 10
    for i, line in enumerate(picture.split('\n')):
        y = y0 + i*dy
        frame= cv2.putText(frame, line, (0, y ), font,
                    fontScale, color, thickness, cv2.FONT_HERSHEY_PLAIN)
    return frame

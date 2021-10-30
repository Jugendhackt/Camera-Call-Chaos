import cv2

def ascii(frames):






    
    scale = 9/255
    gscale1 = "@%#*+=-:. "
    gscale = []
    for i3 in gscale1:
        gscale.append(i3)
    picture = ""
    
    for i in frames:
    
        #print(i*scale)
        
        for i2 in i*scale:
            #print(gscale[int(i2)])
            picture = picture +gscale[int(i2)]

        picture = picture +" \n "
    return picture

    


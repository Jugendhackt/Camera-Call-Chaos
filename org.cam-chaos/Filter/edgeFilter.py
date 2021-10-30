import numpy as np
import cv2

def edgeFilter(frame):
    ksize = (0, 10)
    
    
    edges = cv2.Canny(frame,100,70)
    res2 = cv2.Canny(frame,1,1)
    ret, mask = cv2.threshold(res2, 0, 255,cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
    frame[mask == 255] = [0, 0, 0]
    #frame[mask == 0] = [0, 150, 0]
    return frame



import pyvirtualcam
import numpy as np
import cv2 as cv
from jpeg_artifacts import jpeg_corruption, jpeg_compression

frames = []
current_frame = 0
frame_count = 0
forward = False

def loop(frame, rec, glitch):
    global current_frame, forward, frame_count, frames
    if rec:
        frames.append(frame)
        current_frame = len(frames) - 1
        return frame

    elif frames:
        if glitch:
            frame_count+=1
            if frame_count < 10:
                return jpeg_corruption(frame)
            frame_count = 0
            frames = []
            forward = False
            return frame


        else:
            current_frame += 1 if forward else -1
            if current_frame - 1 <= 0 or current_frame >= len(frames):
                forward = not forward
            print(current_frame)
            return frames[current_frame - 1]
    else:
        return frame

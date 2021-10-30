import pyvirtualcam
import numpy as np
import cv2 as cv

from jpeg_artifacts import jpeg_corruption, jpeg_compression

capture = cv.VideoCapture(0)
fmt = pyvirtualcam.PixelFormat.BGR

if __name__ == "__main__":
    with pyvirtualcam.Camera(1280, 720, 20, fmt=fmt) as cam:
        print(f'Using virtual camera: {cam.device}')

        while True:
            isTrue, frame = capture.read()
            frame = jpeg_corruption(frame)
            cam.send(frame)
            cam.sleep_until_next_frame()

    capture.release()
    cv.destroyAllWindows()

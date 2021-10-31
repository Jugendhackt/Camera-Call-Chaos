import pyvirtualcam
import numpy as np
import cv2 as cv
import pathlib
import os
from jpeg_artifacts import jpeg_corruption, jpeg_compression
from loop import loop




capture = cv.VideoCapture(os.environ["WEBCAM_INDEX"] if "WEBCAM_INDEX" in os.environ
                          else 0)
fmt = pyvirtualcam.PixelFormat.BGR

if __name__ == "__main__":
    with pyvirtualcam.Camera(1280, 720, 20, fmt=fmt) as cam:
        print(f'Using virtual camera: {cam.device}')

        while True:
            isTrue, frame = capture.read()
            frame = np.flip(frame, axis=1)
            frame = loop(frame, pathlib.Path("recording").exists(), pathlib.Path("glitch").exists())
            cam.send(frame)
            cam.sleep_until_next_frame()

    capture.release()
    cv.destroyAllWindows()

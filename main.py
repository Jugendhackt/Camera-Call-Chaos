import pyvirtualcam
import numpy as np
import cv2 as cv
import pathlib
import os
>>>>>>> 70406ef1848d6f6aea4bd0a1f79f18d7de57b4ee
from jpeg_artifacts import jpeg_corruption, jpeg_compression
from loop import loop


def run(state):
    capture = cv.VideoCapture(os.environ["WEBCAM_INDEX"] if "WEBCAM_INDEX" in os.environ
                              else 0)
    fmt = pyvirtualcam.PixelFormat.BGR
    WIDTH = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
    HEIGHT = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))

    with pyvirtualcam.Camera(WIDTH, HEIGHT, 20, fmt=fmt, device="/dev/video0") as cam:
        print(f'Using virtual camera: {cam.device}')

        while True:
            isTrue, frame = capture.read()
            frame = np.flip(frame, axis=1)
            frame = loop(frame, pathlib.Path("recording").exists(), pathlib.Path("glitch").exists())
            state.recording
            frame = jpeg_corruption(frame)
            cam.send(frame)
            cam.sleep_until_next_frame()

    capture.release()
    cv.destroyAllWindows()

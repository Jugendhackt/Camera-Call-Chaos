import pyvirtualcam
import numpy as np
import cv2 as cv
import pathlib
import os
import torch
from Filter.jpeg_artifacts import jpeg_corruption, jpeg_compression
from Filter.animalfilter import animalfilter
from Filter.Ascii import ascii
from Filter.binary import binary
from Filter.blurfilter import blurfilter
from Filter.edgeFilter import edgeFilter
from Filter.pixelError import pixelError
from Filter.waterfilter import waterfilter
from loop import loop

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def run(state):
    capture = cv.VideoCapture(os.environ["WEBCAM_INDEX"] if "WEBCAM_INDEX" in os.environ
                              else 0)
    fmt = pyvirtualcam.PixelFormat.BGR
    WIDTH = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
    HEIGHT = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))

    with pyvirtualcam.Camera(WIDTH, HEIGHT, 20, fmt=fmt) as cam:
        print(f'Using virtual camera: {cam.device}')

        while True:
            isTrue, frame = capture.read()
            frame = np.flip(frame, axis=1)

            frame = loop(frame, state.recording, state.glitch)

            if state.filter == "animalfilter":
                frame = animalfilter(frame, model)
            elif state.filter == "jpeg_compression":
                frame = jpeg_compression(frame)
            elif state.filter == "jpeg_corruption":
                frame = jpeg_corruption(frame)
            elif state.filter == "ascii":
                frame = ascii(frame, WIDTH, HEIGHT)
            elif state.filter == "binary":
                frame = binary(frame, WIDTH, HEIGHT)
            elif state.filter == "blurfilter":
                frame = blurfilter(frame, model)
            elif state.filter == "edgeFilter":
                frame = edgeFilter(frame)
            elif state.filter == "pixelError":
                frame = pixelError(frame)
            elif state.filter == "waterfilter":
                frame = waterfilter(frame)

            cam.send(frame)
            cam.sleep_until_next_frame()

    capture.release()
    cv.destroyAllWindows()

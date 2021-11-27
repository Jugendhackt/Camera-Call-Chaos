from PIL import Image
from io import BytesIO
import numpy as np


def jpeg_corruption(frame):
    img = Image.fromarray(frame)
    with BytesIO() as f:
        img.save(f, format='JPEG', quality=30)
        f.seek(0)
        b = bytearray(f.read())
        co = int(len(b)/10)
        b[1000:co*2] = b[1000+co*6:co*8]
        img = Image.open(BytesIO(b))
    try:
     return np.array(img)
    except OSError:
     return jpeg_compression(frame)


def jpeg_compression(frame):
    img = Image.fromarray(frame)
    with BytesIO() as f:
        img.save(f, format='JPEG', quality=1)
        f.seek(0)
        img = Image.open(f)
        img.load()
        img.save(f, format='JPEG', quality=1)
        f.seek(0)
        img = Image.open(f)
        img.load()
        img.save(f, format='JPEG', quality=1)
        f.seek(0)
        img = Image.open(f)
        img.load()

    return np.array(img)

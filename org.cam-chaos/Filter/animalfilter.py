import cv2
from PIL import Image
import numpy as np

#model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
def animalfilter(frame, model):

    image = Image.open("Animal.jpg")

    img = frame;
    h, w, c = img.shape
    result = model(img)
    mWidth = 0
    result_img0 = result.xyxy[0]
    for detection in result_img0:
        xmin = detection[0]
        xmax = detection[2]

        width = int(xmax) - int(xmin)
        mWidth = max(width, mWidth)
    for detection in result_img0:
        xmin = detection[0]
        ymin = detection[1]
        xmax = detection[2]
        ymax = detection[3]
        conf = float(detection[4])

        size = (width, int(ymax)-int(ymin))
        animal_pic_out = image.resize(size)

        width = int(xmax) - int(xmin)
        name = result.names[int(detection[5])]
        if conf >= 0.5 and name == "person":
            if width == mWidth:
                label = '%s: %d%%' % (name, int(conf * 100))
                cv2.putText(frame, label, (int(xmin), int(ymin)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
                cv2.rectangle(frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 100), 5)
            else:
                an_frame = animal_pic_out
                frame[int(ymin):int(ymax), int(xmin):int(xmax)] = np.asanyarray(an_frame)
    return frame

vid = cv2.VideoCapture(0)
while True:
    ret, frame = vid.read()

    frame1 = animalfilter(frame)

    cv2.imshow('frame', frame1)

    if cv2.waitKey(1) == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()

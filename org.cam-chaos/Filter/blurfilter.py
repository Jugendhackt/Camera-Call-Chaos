import cv2
import torch

def blurfilter(frame):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    img = frame
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

        width = int(xmax) - int(xmin)
        name = result.names[int(detection[5])]
        if conf >= 0.5 and name == "person":
            if width == mWidth:
                label = '%s: %d%%' % (name, int(conf * 100))
                cv2.putText(frame, label, (int(xmin), int(ymin)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
                cv2.rectangle(frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 100), 5)
            else:
                blur_frame = cv2.GaussianBlur(img[int(ymin):int(ymax), int(xmin):int(xmax)], (11, 11), 10, 10,
                                              cv2.BORDER_REFLECT)
                frame[int(ymin):int(ymax), int(xmin):int(xmax)] = blur_frame

    return frame

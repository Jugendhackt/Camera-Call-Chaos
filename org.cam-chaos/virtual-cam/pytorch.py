import torch
import cv2

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Images
#imgs = ['https://ultralytics.com/images/zidane.jpg']  # batch of images

# Inference
#results = model(imgs)

# Results
#print(results)
#results.print()
#results.save()  # or .show()

#results.xyxy[0]  # img1 predictions (tensor)
#results.pandas().xyxy[0]  # img1 predictions (pandas)
#      xmin    ymin    xmax   ymax  confidence  class    name
# 0  749.50   43.50  1148.0  704.5    0.874023      0  person
# 1  433.50  433.50   517.5  714.5    0.687988     27     tie
# 2  114.75  195.75  1095.0  708.0    0.624512      0  person
# 3  986.00  304.00  1028.0  420.0    0.286865     27     tie

vid = cv2.VideoCapture(0);
while True:
    ret, frame = vid.read();

    img = frame;
    h, w, c = img.shape
    result = model(img)

    mWidth = 0
    #result.xyxy[0]  # img1 predictions (tensor)
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
        if conf >= 0.5 and name == "person" :
            if width == mWidth:
                label = '%s: %d%%' % (name, int(conf * 100))
                cv2.putText(frame, label, (int(xmin), int(ymin)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
                cv2.rectangle(frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 100), 5)
            else:
                blur_frame = cv2.GaussianBlur(img[int(ymin):int(ymax), int(xmin):int(xmax)], (11, 11), 10, 10, cv2.BORDER_REFLECT)
                frame[int(ymin):int(ymax), int(xmin):int(xmax)] = blur_frame

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
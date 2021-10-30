import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Images
def analyseImage(image):
    imgs = [image]  # batch of images

    # Inference
    results = model(imgs)

    # Results
    #test = results.print()
    #results.show()  # or .show()

    #results.xyxy[0]  # img1 predictions (tensor)
    test = results.pandas().xyxy[0]
    test2 = results.xyxy[0]
    res = 0.0
    for i2 in test2:
        res = float(i2[4])

    if results.names[0] == "person" and res >= 0.5:
        return "person"
    else:
        return "no person"

    

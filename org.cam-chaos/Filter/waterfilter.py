import cv2

def waterfilter(frame):
    res = cv2.stylization(frame, sigma_s=100, sigma_r=0.6)
    return res


vid = cv2.VideoCapture(0)
while True:
    ret, frame = vid.read()
    frame1 = waterfilter(frame)
    cv2.imshow('frame', frame1)

    if cv2.waitKey(1) == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
import cv2
cam = cv2.VideoCapture(0)
while cam.isOpened():
    state, frame = cam.read()
    if not state:
        print('no frame')
        break
    cv2.imshow('cam1', frame)
    if cv2.waitKey(1) == ord('q'):
     break
cam.release()
cv2.destroyAllWindows()
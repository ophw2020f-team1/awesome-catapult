import numpy as np
import cv2
from moocxing.package import MOOCXING
from moocxing.robot.Brain import Brain

mx = MOOCXING()

media = mx.initMedia()

serial = mx.initSerial(com="COM4", bps=9600)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    img = frame #shape(480,640,3)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #print(faces)
    for (x, y, w, h) in faces: # 如果有两张脸的话需要另外调试
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        servo_positionx = 2 * (x + w / 2) / 480 - 1
        servo_positiony = 2 * (y + h / 2) / 640 - 1
    cv2.imshow('img', img)
    key = cv2.waitKey(200)
    if key == ord('q'):
        break

    serial.send(int(servo_positionx*60))

cv2.destroyAllWindows()
cap.release()

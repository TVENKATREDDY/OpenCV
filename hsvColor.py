import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('img',hsv_frame)
    if cv2.waitKey(0) == 27:
        break
    cv2.inRange
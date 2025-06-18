import cv2
import numpy as np
cap=cv2.VideoCapture(r'C:\Venkat\Python\Practice_Material\DEEP LEARNING(10th Jan)\29th Jan\8. Object tracking from scratch\8. Object tracking from scratch\Object-tracking-from-scratch-source_code\source_code\los_angeles.mp4')
_,frame=cap.read()
img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
cv2.imshow('Frame',img_gray)
cv2.waitKey(0)
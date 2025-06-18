import cv2
import numpy as np
body_classifier=cv2.CascadeClassifier(r'C:\Users\91807\VSCodeProjects\PythonPractice\10. OPEN CV\haarcascade_fullbody.xml')
cap=cv2.VideoCapture(r'C:\Venkat\Venkat_Photos\27260-362770008_tiny.mp4')
while cap.isOpened():
    ret,frame=cap.read()
    print('frame :',frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    bodies=body_classifier.detectMultiScale(gray,1.2,3)
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.inshow('Pedestrian',frame)
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()
import cv2
face_classifier=cv2.CascadeClassifier(r'C:\Users\91807\VSCodeProjects\PythonPractice\10. OPEN CV\haarcascade_frontalface_default.xml')
ey_classifier=cv2.CascadeClassifier(r'C:\Users\91807\VSCodeProjects\PythonPractice\10. OPEN CV\haarcascade_eye.xml')
def detect(gray,frame):
    faces=face_classifier.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=ey_classifier.detectMultiScale(roi_gray,1.1,3)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
        return frame
vedio_capture=cv2.VideoCapture(0)
while True:
    _, frame=vedio_capture.read()
    frame=cv2.resize(frame,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)
    #print(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas=detect(gray,frame) 
    cv2.imshow('Video',canvas)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
vedio_capture.release()
cv2.destroyAllWindows()
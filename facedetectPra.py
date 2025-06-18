import numpy as np
import cv2
facedetectClassifier=cv2.CascadeClassifier(r'C:\Users\91807\VSCodeProjects\PythonPractice\10. OPEN CV\haarcascade_frontalface_default.xml')
image=cv2.imread(r'C:\Users\91807\Downloads\tvr_photo.jpeg')

if image is None:
    print('Error:Image not found')
    exit()

#convert the image to grayscale
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces=facedetectClassifier.detectMultiScale(gray,1.3,5)

#check if faces are detected
if len(faces)==0:
    print('No faces found')
else:
    #draw rectangle around the face
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(60,0,60),2)
        #cv2.circle(image,radius=x+y,center=(x,y),color=cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('image',image)
    cv2.waitKey()
    
cv2.destroyWindow()

import cv2
face_classifier=cv2.CascadeClassifier(r'-C:\Users\91807\VSCodeProjects\PythonPractice\10. OPEN CV\haarcascade_frontalface_default.xml')
eye_classifier=cv2.CascadeClassifier(r'C:\Users\91807\VSCodeProjects\PythonPractice\10. OPEN CV\haarcascade_eye.xml')
img=cv2.imread(r'C:\Users\91807\Downloads\tvr_photo.jpeg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_classifier.detectMultiScale(img,1.3,5)
if len(faces)==0:
    print('No Face Found')
    exit()
else:
    print('faces: ',faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        #cv2.imshow('image',img)
        #cv2.waitKey()
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        print('original',gray)
        print('gray: ',roi_gray)
        print('color: ',roi_color)
        eyes=eye_classifier.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(225,0,255),2)
            cv2.imshow('img',img)
            cv2.waitKey()
cv2.destroyWindow()
import cv2
cap=cv2.VideoCapture(r'C:\Venkat\Python\Practice_Material\DEEP LEARNING(10th Jan)\29th Jan\8. Object tracking from scratch\8. Object tracking from scratch\Object-tracking-from-scratch-source_code\source_code\los_angeles.mp4')
while True:
    ret,frame=cap.read()
    cv2.imshow('frame',frame)
    key=cv2.waitKey(0)
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()


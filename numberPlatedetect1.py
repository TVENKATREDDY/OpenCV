import cv21
import imutils
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Venkat\Python\Practice_Material\DEEP LEARNING(10th Jan)\30th Jan OCR and Color Detect\28. Number plate detection\28. Number plate detection'
img=cv2.imread(r'C:\Venkat\Python\Practice_Material\DEEP LEARNING(10th Jan)\30th Jan OCR and Color Detect\28. Number plate detection\28. Number plate detection\jeep.jpg')
resized_image=imutils.resize(img)
cv2.imshow('img',img)
cv2.waitKey(0)
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image',gray_image)
cv2.waitKey(0)
gray_image=cv2.bilateralFilter(gray_image,11,17,17)
cv2.imshow('smoothened img',gray_image)
cv2.waitKey(0)
edged=cv2.Canny(gray_image,30,200)
cv2.imshow('edged image',edged)
cv2.waitKey(0)

cnts,new=cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
img1=img.copy()
cv2.drawContours(img1,cnts,-1,(0,255,0),3)
cv2.imshow('Contours',img1)
cv2.waitKey(0)

cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:30]
screenCnt=None
img2=img.copy()
cv2.drawContours(img2,cnts,-1,(0,255,0),3)
cv2.imshow('top 30 contours',img2)
cv2.waitKey(0)
i=7
for c in cnts:
    perimeter=cv2.arcLength(c,True)
    print(perimeter)

    approx=cv2.approxPolyDP(c,0.018 * perimeter,True)
    print(approx)
    '''
    if len(approx)==4:
        screenCnt=approx
        x,y,w,h=cv2.boundingRect(c)
        new_img=img[y:y+h,x:x+w]
        cv2.imwrite('./'+str(i)+'.png',new_img)
        i+=1
        break
    '''
cv2.drawContours(img,[screenCnt],-1,(0,255,0),3)
cv2.imshow('Image with num plate',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



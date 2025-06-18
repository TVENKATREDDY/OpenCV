import cv2
input=cv2.imread(r'C:\Venkat\Python\Practice_Material\DEEP LEARNING(10th Jan)\21 Jan CNN Practical\CNN Practical\testing\Happy1.jpeg')

cv2.imshow('Happy',input)
print('Height of Image:',int(input.shape[0]),'pixels')
print('Width of Image:',int(input.shape[1]),'pixels')
cv2.waitKey()
cv2.destroyWindow(winname='test')

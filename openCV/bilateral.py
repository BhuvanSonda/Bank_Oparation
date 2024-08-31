import cv2 as cv

img=cv.imread('openCV/cat.jpg',0)
print('original image',img)

blur=cv.bilateralFilter(img,10,50,50)
print('blurred image',blur)
cv.imshow('original',img)
box=cv.GaussianBlur(img,(5,5),3,borderType=3)
cv.imshow('Gaussian blur',box)

cv.imshow('Bilateral Filter',blur)



b=cv.boxFilter(img,cv.CV_8U,(5,5))
cv.imshow('Box Filter',b)
cv.waitKey(0)
cv.destroyAllWindows()
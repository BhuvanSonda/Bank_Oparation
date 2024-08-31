import cv2 as cv

img=cv.imread('famer.jpg',0)
cv.imshow('Original Image',img)

blr=cv.blur(img,(21,21),anchor=(3,3))
cv.imshow('Blurred Image',blr)

blur=cv.blur(img,(21,21))
cv.imshow(' Image',blur)

median_blr=cv.medianBlur(img,(5))
cv.imshow('Median Blurred Image',median_blr)

guasian=cv.GaussianBlur(img,(11,11),cv.BORDER_DEFAULT)
cv.imshow('Gaussian Blurred Image',guasian)

box=cv.boxFilter(img,ddepth=-1,ksize=(5,5),normalize=True)
cv.imshow('boxFilter',box)

cv.waitKey(0)
cv.destroyAllWindows()

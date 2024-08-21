import cv2 as cv

img=cv.imread('famer.jpg',1)
cv.imshow('Original Image',img)

blr=cv.blur(img,(21,21))
cv.imshow('Blurred Image',blr)

median_blr=cv.medianBlur(img,(5))
cv.imshow('Median Blurred Image',median_blr)

guasian=cv.GaussianBlur(img,(11,11),cv.BORDER_DEFAULT)
cv.imshow('Gaussian Blurred Image',guasian)


cv.waitKey(0)
cv.destroyAllWindows()

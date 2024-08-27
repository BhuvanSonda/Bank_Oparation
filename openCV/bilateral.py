import cv2 as cv

img=cv.imread('openCV/cat.jpg',0)

blur=cv.bilateralFilter(img,9,75,75)

cv.imshow('original',img)
cv.imshow('blurred',blur)
cv.waitKey(0)
cv.destroyAllWindows()
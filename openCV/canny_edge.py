import cv2 as cv

image=cv.imread('openCV/cat.jpg',0)
edg=cv.Canny(image,200,200)
cv.imshow('Original',image)
cv.imshow('edges',edg)
cv.waitKey(0)
cv.destroyAllWindows()


import cv2 as cv

img=cv.imread('bank.png',1)
angle=180
scale= 1.0#None
(h,w)=img.shape[:2]
centre=(w/2,h/2)
print(img.shape[2])

matrix=cv.getRotationMatrix2D( centre, angle, scale)
rotation=cv.warpAffine(img,matrix,(w,h))

#rotation=cv.rotate(img,cv.ROTATE_90_CLOCKWISE)

cv.imshow('Original Image',img)
cv.imshow('Rotation Image',rotation)
cv.waitKey(0)
cv.destroyAllWindows()
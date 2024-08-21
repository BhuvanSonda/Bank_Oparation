import cv2 as cv
 
img=cv.imread('dog.jpg',1)
cv.imshow('Original image',img)

percent=200
width=int(img.shape[1]* percent/100)
height=int(img.shape[0]* percent/100)
dim=(width,height)

resized= cv.resize(img,dim,interpolation=cv.INTER_CUBIC)
cv.imshow('Resized image',resized)

border_color = [0, 255, 255] 
border=cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_CONSTANT,value=border_color)
cv.imshow('Bordered image',border)

cv.waitKey(0)
cv.destroyAllWindows()
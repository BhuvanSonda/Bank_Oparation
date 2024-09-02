import cv2 as cv
import numpy as np

img=cv.imread('famer.jpg',-1)

kernel=np.ones((5,5),np.uint8)
print("kernel =",kernel)
d_img=cv.dilate(img,kernel,iterations=1)

E_img=cv.erode(img,kernel,iterations=1)

cv.imshow('original',img)
cv.imshow("dilated image",d_img)
cv.imshow("eroded image",E_img)
cv.waitKey(0)
cv.destroyAllWindows()
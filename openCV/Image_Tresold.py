import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread("famer.jpg",0)

r,t=cv.threshold(img,55,300,cv.THRESH_BINARY)
print(img[])

cv.imshow("original",img)
cv.imshow("Thresold",t)
cv.waitKey(0)
cv.destroyAllWindows()
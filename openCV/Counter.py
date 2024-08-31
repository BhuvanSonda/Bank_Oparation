import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img= cv.imread("openCV/cat.jpg",0)


ret,binary=cv.threshold(img,100,255,cv.THRESH_BINARY)

counters,hierarchy=cv.findContours(binary,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
cv.drawContours(img,counters,-1,(0,225,0),2)
# print(hierarchy)

plt.subplot()
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')


cv.imshow("Counters",img)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
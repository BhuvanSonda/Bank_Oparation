import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

imge=cv.imread("famer.jpg",1)
img=cv.cvtColor(imge,cv.COLOR_BGR2GRAY)
temp=cv.imread("famer_animal.jpg",0)
w,h=np.shape(temp)
print(w,h)

res = cv.matchTemplate(img,temp,cv.TM_CCOEFF_NORMED)
tres=.9

loc = np.where(res >= tres)   
   
for pt in zip(*loc[::-1]):   
    cv.rectangle(imge, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)   
    
# plt.subplot()
# plt.imshow(imge)
# plt.title("matched Templates")
# plt.show()

cv.imshow('Detected',imge) 
cv.waitKey(0) 
cv.destroyAllWindows()


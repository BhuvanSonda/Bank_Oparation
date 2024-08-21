import cv2 as cv

img=cv.imread('python.jpg',1)

image=cv.line(img,(0,0),(50,50),(0,0,255),5)

image=cv.rectangle(img,(50,50),(100,100),(0,0,255),5)

image=cv.arrowedLine(img,(100,100),(150,150),(0,0,255),5)

cv.circle(img,(150,150),50,(0,0,255),5)

font=cv.FONT_HERSHEY_TRIPLEX
cv.putText(img,'Python',(0,200),font,1,(0,25,20),2,cv.LINE_AA)

cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()
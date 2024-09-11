import cv2 as cv

img=cv.imread('search_4.png',1)
cv.namedWindow('Rotation Image')

angle=360
scale= 1.5
(h,w)=img.shape[:2]
centre=(w/2,h/2)
while True:
    brk=0
    for angle in range(360):
        if cv.waitKey(1)&0xFF==ord("q"):
            brk=1
            break
        if angle==360:
            
            angle=0
            
       
        M=cv.getRotationMatrix2D(centre, angle, scale)
        rotation=cv.warpAffine(img,M,(w,h))
        cv.imshow('Rotation Image',rotation)
    if brk ==1:
        break
    

cv.destroyAllWindows()
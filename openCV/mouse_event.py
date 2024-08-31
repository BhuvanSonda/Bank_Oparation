import cv2 as  cv
import numpy as np
import matplotlib as plt

def draw(event,x,y,flag,params):
    if event == cv.EVENT_LBUTTONDOWN:
        #cv.putText(img, (f"{x},{y}"), (x, y), cv.FONT_HERSHEY_TRIPLEX,0.5, (0, 0, 255), 2, cv.LINE_8)
        cv.circle(img,(x,y),20,(0,0,255),-1)

img=cv.imread('openCV/cat.jpg',1)
cv.namedWindow('image')
cv.setMouseCallback('image',draw)
while True:
    cv.imshow('image',img)
    if cv.waitKey(1) & 0xFF== ord('q'):
        break
cv.destroyAllWindows()
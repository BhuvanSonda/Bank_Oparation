
import cv2 as cv
import numpy as np


# Load the cascade classifier for face detection
cas = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

# Load the image in grayscale
# img = cv.imread('virat.jpg') 
# Gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# # Detect faces in the image
# faces = cas.detectMultiScale(Gray, scaleFactor=1.1, minNeighbors=5)

# # Draw rectangles around the detected faces
# for (x, y, w, h) in faces:
#     cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# # Display the image with detected faces
# cv.imshow('face recognition', img)

# # Wait for the 'q' key to be pressed to close the window
# cv.waitKey(0)

import dlib
vdo=cv.VideoCapture(0)#Assign vdo capturing to camera index 0
while True:
    ret,frame=vdo.read()#for load the vdo frame
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)#for convert colored innto gray scale
    faces=cas.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)#for detect the face
    for (x,y,w,h) in faces:#find the position of the face and draw rectangle on the detected face
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv.imshow('face',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
vdo.release()#For release the vdo capturing memory


cv.destroyAllWindows()# for clse the window
                     
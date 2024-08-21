#importing the opencv module
import cv2 as cv  
import os

path = os.path.abspath('cat.jpg')
print("file path",path)
print(os.getcwd())

# using imread('path') and 1 denotes read as  color image  
img = cv.imread('black_and_white.jpg',1) 
# img = cv.imread('black_and_white.jpg',-1) 
pix=img[23,10] 
(h,w)=img.shape[:2]
print(f"x={h},y={w}")
#

print(pix)
#This is using for display the image  
cv.imshow('image',img)  
key=cv.waitKey() # This is necessary to be required so that the image doesn't close immediately.  
#It will run continuously until the key press.  

cv.imwrite("image_copy.png",img)
cv.destroyAllWindows()
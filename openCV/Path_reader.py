import os
import cv2 as cv

# Name of the searching  file 
file_name = 'cat.jpg'

#get the main directory
start_dir = os.getcwd()

# Search for the file
file_path = None
for root, dirs, files in os.walk(start_dir):
    if file_name in files:
        file_path = os.path.join(root, file_name)
        break

if file_path:
    print("\nFile found = ", file_path,"\n")
    img = cv.imread(file_path,0) 
    cv.imshow('image',img)  
    key=cv.waitKey()
    cv.destroyAllWindows()
else:
    print("\nFile not found!!")


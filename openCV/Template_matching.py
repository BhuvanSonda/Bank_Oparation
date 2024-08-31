# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt

# img=cv.imread("famer.jpg",0)

# temp=cv.imread("famer.jpg",0)
# w,h=np.shape(temp)
# print(w,h)

# res = cv.matchTemplate(img,temp,cv.TM_CCOEFF)
# tres=0.8
# # We want to find the best match in the entire image. So we don't specify any area
# min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
# # Now max_loc contains the top left coordinates of the best match

# oc = np.where(res >= tres)   
# # Draw the rectangle around the matched region.   
# for pt in zip(*max_loc[::-1]):   
#     cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)   
# # Now display the final matched template image   
# cv.imshow('Detected',img) 
# cv.waitKey(0) 
# cv.destroyAllWindows()
import cv2
import numpy as np

# Load the main image and the template image
image = cv2.imread('famer.jpg',0)
template = cv2.imread('famer_animal.jpg',0)

# # Convert both images to grayscale
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Get the width and height of the template image
w, h = np.shape(template)

# Perform template matching using the cv2.matchTemplate function
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

# Set a threshold for detection
threshold = 0.8

# Find locations where the result is greater than the threshold
locations = np.where(result >= threshold)

# Draw rectangles on the matched regions
for pt in zip(*locations[::-1]):
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

# Display the result
cv2.imshow('Detected Template', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

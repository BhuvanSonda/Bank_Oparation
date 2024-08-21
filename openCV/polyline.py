import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Define points for the triangle
poly = np.array([[90,50],[100,200],[500,200],[300,100]], np.int32)

# Draw the polyline
cv2.polylines(img, [poly], isClosed=True, color=(0, 255, 0), thickness=3)

# Display the image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

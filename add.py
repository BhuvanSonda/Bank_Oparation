import cv2

# Load image
img = cv2.imread('openCV/cat.jpg')

# Split the channels
b, g, r = cv2.split(img)
print(r)

# Modify the red channel to correct color imbalance
r = cv2.add(r, -50)  # Reduce red intensity
print("\nedited",r)
# Merge channels back together
corrected_img = cv2.merge((b, g, r))

# show the image
cv2.imshow('Edited image',corrected_img)
cv2.imshow('Original Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt

# # Read the image in grayscale
# img = cv.imread("temple_run.jpg", 0)

# # Convert the grayscale image to BGR for displaying contours
# colored_img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
# colored_img_1 = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

# # Apply binary thresholding
# ret, binary = cv.threshold(img, 100, 255, cv.THRESH_BINARY)

# # Find contours
# # c, h = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
# c, h = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# # c, h = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

# # Draw contours on the image
# cv.drawContours(colored_img_1, c, -1, (0, 0, 255), 2)

# print(f"Number of contours found: {len(c)}")

# # Convert BGR images to RGB for displaying with Matplotlib
# colored_img_rgb = cv.cvtColor(colored_img, cv.COLOR_BGR2RGB)
# colored_img_1_rgb = cv.cvtColor(colored_img_1, cv.COLOR_BGR2RGB)

# # Display images using Matplotlib
# plt.figure(figsize=(10, 5))

# plt.subplot(1, 2, 1)
# plt.imshow(colored_img_rgb)
# plt.title('Original Image')
# plt.axis('off')

# plt.subplot(1, 2, 2)
# plt.imshow(colored_img_1_rgb)
# plt.title('Image with Contours')
# plt.axis('off')

# plt.show()

# # Display images using OpenCV
# cv.imshow("Original Image", colored_img)
# cv.imshow("Contours", colored_img_1)

# cv.waitKey(0)
# cv.destroyAllWindows()
import cv2 as cv
import numpy as np

# Read the image in grayscale
img = cv.imread("temple_run.jpg", 0)

# Apply binary thresholding
ret, binary = cv.threshold(img, 100, 255, cv.THRESH_BINARY)

contours_simple, _ = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)# Find contours with cv.CHAIN_APPROX_SIMPLE
print(f"Number of contours with cv.CHAIN_APPROX_SIMPLE: {len(contours_simple)}")


contours_none, _ = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)# Find contours with cv.CHAIN_APPROX_NONE
print(f"Number of contours with cv.CHAIN_APPROX_NONE: {len(contours_none)}")

# Optional: Draw contours on images to visualize
colored_img_simple = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
cv.drawContours(colored_img_simple, contours_simple, -1, (0, 255, 0), 2)

colored_img_none = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
cv.drawContours(colored_img_none, contours_none, -1, (0, 255, 0), 2)

# Display images with contours using OpenCV
cv.imshow("Contours with cv.CHAIN_APPROX_SIMPLE", colored_img_simple)
cv.imshow("Contours with cv.CHAIN_APPROX_NONE", colored_img_none)

cv.waitKey(0)
cv.destroyAllWindows()

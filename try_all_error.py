# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # Load an example image
# image = cv2.imread('famer.jpg')

# # Convert image to RGB format for displaying using matplotlib (OpenCV uses BGR format)
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Gaussian Blur with different sigma values
# gaussian_blur_sigma1 = cv2.GaussianBlur(image, (15, 15), sigmaX=1)
# gaussian_blur_sigma5 = cv2.GaussianBlur(image, (15, 15), sigmaX=5)

# # Bilateral Filter with different sigma values
# bilateral_filter_sigma10 = cv2.bilateralFilter(image, d=9, sigmaColor=10, sigmaSpace=10)
# bilateral_filter_sigma50 = cv2.bilateralFilter(image, d=9, sigmaColor=500, sigmaSpace=500)

# # Convert blurred images to RGB for displaying
# gaussian_blur_sigma1_rgb = cv2.cvtColor(gaussian_blur_sigma1, cv2.COLOR_BGR2RGB)
# gaussian_blur_sigma5_rgb = cv2.cvtColor(gaussian_blur_sigma5, cv2.COLOR_BGR2RGB)
# bilateral_filter_sigma10_rgb = cv2.cvtColor(bilateral_filter_sigma10, cv2.COLOR_BGR2RGB)
# bilateral_filter_sigma50_rgb = cv2.cvtColor(bilateral_filter_sigma50, cv2.COLOR_BGR2RGB)

# # Display the images
# plt.figure(figsize=(12, 8))

# plt.subplot(2, 3, 1)
# plt.imshow(image_rgb)
# plt.title('Original Image')
# plt.axis('off')

# plt.subplot(2, 3, 2)
# plt.imshow(gaussian_blur_sigma1_rgb)
# plt.title('Gaussian Blur, Sigma = 1')
# plt.axis('off')

# plt.subplot(2, 3, 3)
# plt.imshow(gaussian_blur_sigma5_rgb)
# plt.title('Gaussian Blur, Sigma = 5')
# plt.axis('off')

# plt.subplot(2, 3, 5)
# plt.imshow(bilateral_filter_sigma10_rgb)
# plt.title('Bilateral Filter, Sigma = 10')
# plt.axis('off')

# plt.subplot(2, 3, 6)
# plt.imshow(bilateral_filter_sigma50_rgb)
# plt.title('Bilateral Filter, Sigma = 50')
# plt.axis('off')

# plt.show()
import cv2
import numpy as np

# Load the main image and the template image in grayscale
image = cv2.imread('famer.jpg', )
template = cv2.imread('famer_animal.jpg', 0)

# Check if images are loaded successfully
if image is None or template is None:
    print("Error loading images.")
    exit()

# Get the dimensions of the template image
h, w = template.shape

# Perform template matching using the normalized cross-correlation method
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

# Set a threshold for the template matching results
threshold = 0.8

# Find locations in the result array where values are above the threshold
locations = np.where(result >= threshold)

# Draw rectangles around matched regions on the original image
for pt in zip(*locations[::-1]):
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

# Display the result with detected regions
cv2.imshow('Detected Template', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
